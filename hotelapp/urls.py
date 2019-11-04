from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation-form', views.registration_form, name='registrationForm'),
    path('new-customer', views.new_customer_form, name='new-customer')
]
