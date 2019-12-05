from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('reservation-form', views.registration_form, name='reservation-form'),
    path('new-customer', views.new_customer_form, name='new-customer'),
    path('find-room', views.find_room, name='find-room'),
    path('select-room', views.select_room, name='reservation-form'),
    path(
        'todays-reservations',
        views.todays_reservations,
        name='todays-reservations'),
    path(
        'reservations',
        views.reservations,
        name='reservations'),
    path('checkout', views.checkout, name='checkout'),
    path('parking-spaces', views.parking_space, name='parking-spaces')
]
