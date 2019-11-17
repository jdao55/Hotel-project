from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation-form', views.registration_form, name='reservation-form'),
    path('new-customer', views.new_customer_form, name='new-customer'),
    path('find-room', views.find_room, name='find-room'),
    path('select-room', views.select_room, name='reservation-form')
]
