from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from . import forms
from . import models
from datetime import date, timedelta
from django.utils import timezone
from django.db import connection


def index(request):
    return render(request, "hotelapp/home.html")


def parking_space(request):
    if request.method == 'POST':
        form = forms.parkingForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            pspaces = models.ParkingSpace.objects.all().filter(
                license_plate__like=form_data['license_plate']).filter(
                    room__isnull=False).select_related(
                        'parking_lot').select_related(
                            'parking_lot__hotel').select_related(
                                'customer').select_related('room')
            return render(request, 'hotelapp/parking_space.html', {
                'form': form,
                'query': pspaces
            })
    else:
        form = forms.parkingForm()
        pspaces = models.ParkingSpace.objects.all().filter(
            room__isnull=False).select_related('parking_lot').select_related(
                'parking_lot__hotel').select_related(
                    'customer').select_related('room')
        return render(request, 'hotelapp/parking_space.html', {
            'form': form,
            'query': pspaces
        })


def registration_form(request):
    if request.method == 'POST':
        form = forms.reserveForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user_id = get_user_id(form_data['name'], form_data['email'],
                                  form_data['phone'])
            new_res = form.save(commit=False)
            new_res.customer_id = user_id
            form.save()
            if form_data['reserve_parking'] is True:
                lot_id = (models.ParkingLot.objects.get(
                    hotel_id=(form_data['room']).hotel_id)).parking_lot_id
                room_id = form_data['room'].room_id

                fn_call = "CALL assign_parking_space({0}, {1}, {2})".format(
                    lot_id, room_id, user_id)
                cursor = connection.cursor()
                cursor.execute(fn_call)

                #update space added
                parking_space = models.ParkingSpace.objects.all().get(
                    Q(parking_lot=lot_id) & Q(room=room_id)
                    & Q(customer=user_id) & Q(car_make='') & Q(
                        license_plate=''))
                parking_space.car_make = form_data['car_make']
                parking_space.license_plate = form_data['license_plate']
                parking_space.save()
            return render(request, "hotelapp/confirmation.html")
    else:
        form = forms.reserveForm()

    return render(request, 'hotelapp/reservation_form.html', {'form': form})


def new_customer_form(request):
    if request.method == 'POST':
        form = forms.createUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = forms.createUserForm()
    return render(request, 'hotelapp/new_user.html', {'form': form})


def find_room(request):
    if request.method == 'POST':
        form = forms.findRoomForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            hotels_list = filter_hotels(form_data)
            room_list = filter_free_rooms(hotels_list, form_data['checkin'],
                                          form_data['checkout'])
            roomForm = forms.selectRoom(initial={
                'checkin': form_data['checkin'],
                'checkout': form_data['checkout']
            })
            return render(request, 'hotelapp/room_list.html', {
                'query': room_list,
                'room': roomForm
            })
    else:
        form = forms.findRoomForm()
    return render(request, 'hotelapp/find_room.html', {'form': form})


def select_room(request):
    if request.method == 'POST':
        form = forms.selectRoom(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            res_form = forms.reserveForm(
                initial={
                    'checkin_date': form_data['checkin'],
                    'checkout_date': form_data['checkout'],
                    'room': form_data['roomid']
                })
            return render(request, 'hotelapp/reservation_form.html',
                          {'form': res_form})


def todays_reservations(request):
    print(date.today())
    todays_res = models.Reservation.objects.all().select_related(
        'customer').select_related('room').select_related(
            'room__hotel').filter(checkin_date__lte=date.today()).filter(
                checkout_date__gte=date.today())
    return render(request, 'hotelapp/list_reservations.html',
                  {'query': todays_res})


def checkout(request):
    if request.method == 'POST':
        form = forms.checkoutForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            res_id = form_data['res_id']
            res = models.Reservation.objects.get(reservation_id=res_id)
            res.delete()

    week = timedelta(days=7)
    res = models.Reservation.objects.all().select_related(
        'customer').select_related('room').select_related(
            'room__hotel').filter(
                checkin_date__lte=timezone.now(),
                checkout_date__lte=(timezone.now() + week))
    checkout_form = forms.checkoutForm()
    return render(request, 'hotelapp/checkout.html', {
        'query': res,
        'form': checkout_form
    })


# filter rooms based on optional filters(pool, gym, breakfast, restaurant)
def filter_hotels(form_data):
    hotels_list = models.Hotel.objects.filter(
        state__icontains=form_data['state']).filter(
            city__icontains=form_data['city'])

    if form_data['has_pool'] != '--':
        if form_data['has_pool'] != 'yes':
            hotels_list = hotels_list.filter(has_pool=True)
        else:
            hotels_list = hotels_list.filter(has_pool=False)

    if form_data['has_gym'] != '--':
        if form_data['has_gym'] != 'yes':
            hotels_list = hotels_list.filter(has_gym=True)
        else:
            hotels_list = hotels_list.filter(has_gym=False)
    if form_data['has_breakfast'] != '--':
        if form_data['has_breakfast'] != 'yes':
            hotels_list = hotels_list.filter(has_breakfast=True)
        else:
            hotels_list = hotels_list.filter(has_breakfast=False)
    if form_data['has_restaurant'] != '--':
        if form_data['has_restaurant'] != 'yes':
            hotels_list.filter(has_restaurant=True)
        else:
            hotels_list = hotels_list.filter(has_restaurant=False)

    return hotels_list


# find rooms in hotel available between checkin and checkout times
def filter_free_rooms(hotels_list, checkin, checkout):
    room_list = models.Room.objects.filter(hotel__in=hotels_list)
    free_rooms = [
        res.room_id for res in models.Reservation.objects.all()
        if is_notfree(res, checkin, checkout)
    ]
    room_list = room_list.exclude(room_id__in=free_rooms)
    return room_list


# probably a better way to do this
def is_notfree(reservation, checkin, checkout):
    q_ci = reservation.checkin_date.date()
    print(type(q_ci))
    q_co = reservation.checkout_date.date()
    if checkin >= q_ci and checkin <= q_co:
        return True
    if checkout >= q_ci and checkout <= q_co:
        return True
    if q_ci >= checkin and q_co <= checkout:
        return True
    return False


# return user_id if email is in data base
# return new user otherwise
def get_user_id(name_, email_, phone_):
    try:
        user = models.Customer.objects.get(email=email_)
        return user.customer_id
    except:
        print("error finding person")
        user = models.Customer.create(name_, email_, phone_)
        user.save()
        return user.customer_id
