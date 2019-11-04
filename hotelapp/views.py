from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def index(request):
    return HttpResponse("Welcome to the hotel reservation app!")


def registration_form(request):
    if request.method == 'POST':
        form = forms.reserveForm(request.POST)
        if form.is_valid():
            reservation_instance = form.save(commit=True)
    else:
        form = forms.reserveForm()
    return render(request, 'hotelapp/reservation_form.html', {'form': form})


def new_customer_form(request):
    if request.method == 'POST':
        form = forms.createUserForm(request.POST)
        if form.is_valid():
            # TODO should add confirmation to web page for adding new user
            reservation_instance = form.save(commit=True)
    else:
        form = forms.createUserForm()
    return render(request, 'hotelapp/new_user.html', {'form': form})
