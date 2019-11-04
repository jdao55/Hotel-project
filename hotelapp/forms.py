from django import forms
from . import models


class reserveForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = [
            'reservation_id', 'checkin_date', 'checkout_date', 'room',
            'customer'
        ]


class createUserForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'email', 'phone']
