from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class ReadonlyDateInput(forms.DateInput):
    input_type = 'date'
    attrs = {'readonly': 'readonly'}


class reserveForm(forms.ModelForm):
    reserve_parking = forms.BooleanField(
        label='reserve parking space', required=False)
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=10)

    class Meta:
        model = models.Reservation
        fields = [
            'reservation_id',
            'checkin_date',
            'checkout_date',
            'room',
        ]
        widgets = {
            'checkin_date': forms.TextInput(attrs={'readonly': 'readonly'}),
            'checkout_date': forms.TextInput(attrs={'readonly': 'readonly'}),
            'room': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class createUserForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'email', 'phone']


class findRoomForm(forms.Form):
    checkin = forms.DateField(widget=DateInput)
    checkout = forms.DateField(widget=DateInput)
    city = forms.CharField(max_length=255)


class selectRoom(forms.Form):
    checkin = forms.DateField(widget=forms.HiddenInput)
    checkout = forms.DateField(widget=forms.HiddenInput)
    roomid = forms.IntegerField(widget=forms.HiddenInput)
