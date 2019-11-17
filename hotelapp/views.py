from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
from django import forms as dforms


def index(request):
    return HttpResponse("Welcome to the hotel reservation app!")


def registration_form(request):
    if request.method == 'POST':
        form = forms.reserveForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = models.Customer.create(
                form_data['name'], form_data['email'], form_data['phone'])
            user.save()
            new_res = form.save(commit=False)
            user_id = user.customer_id
            new_res.customer_id = user_id
            form.save()
            if form_data['reserve_parking'] is True:
                lot_id = (models.ParkingLot.objects.get(
                    hotel_id=(form_data['room']).hotel_id)).parking_lot_id
                room_id = form_data['room'].room_id

                query = "CALL assign_parking_space({0}, {1}, {2})".format(
                    lot_id, room_id, user_id)
                models.ParkingSpace.objects.raw(query)
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
            hotels_list = models.Hotel.objects.filter(city=form_data['city'])
            room_list = models.Room.objects.filter(hotel__in=hotels_list)
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
