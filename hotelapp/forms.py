from django import forms
from . import models

TRUE_FALSE_CHOICES = [('--', '--'), ('yes', 'Yes'), ('no', 'No')]
STATES_CHOICES = [('ON', 'Ontario'), ('AB', 'Alberta'),
                  ('BC', 'British Columbia'), ('MB', 'Manitoba'),
                  ('NB', 'New Brunswick'), ('NL', 'NL'), ('NS', 'Nova Scotia'),
                  ('NT', 'Nunavut'), ('NU', 'Northwest Territories'),
                  ('PE', 'PEI'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'),
                  ('YT', 'Yukon'), ('MI', 'Michigan')]


class DateInput(forms.DateInput):
    input_type = 'date'


class parkingForm(forms.Form):
    license_plate = forms.CharField(
        label='Search my license plate', max_length=10)


class reserveForm(forms.ModelForm):
    reserve_parking = forms.BooleanField(
        label='reserve parking space', required=False)
    license_plate = forms.CharField(
        label='license plate',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        max_length=10,
        required=False)
    car_make = forms.CharField(
        label='car make',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        max_length=20,
        required=False)
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
            'room': forms.HiddenInput()
        }


class createUserForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'email', 'phone']


class findRoomForm(forms.Form):
    checkin = forms.DateField(widget=DateInput)
    checkout = forms.DateField(widget=DateInput)
    city = forms.CharField(max_length=255)
    state = forms.CharField(
        label="Province", widget=forms.Select(choices=STATES_CHOICES))
    has_pool = forms.CharField(
        label='Has Pool', widget=forms.Select(choices=TRUE_FALSE_CHOICES))
    has_gym = forms.CharField(
        label='Has Gym', widget=forms.Select(choices=TRUE_FALSE_CHOICES))
    has_breakfast = forms.CharField(
        label='Has Breakfast', widget=forms.Select(choices=TRUE_FALSE_CHOICES))
    has_restaurant = forms.CharField(
        label='Has Restaurant',
        widget=forms.Select(choices=TRUE_FALSE_CHOICES))


class selectRoom(forms.Form):
    checkin = forms.DateField(widget=forms.HiddenInput)
    checkout = forms.DateField(widget=forms.HiddenInput)
    roomid = forms.IntegerField(widget=forms.HiddenInput)


class checkoutForm(forms.Form):
    res_id = forms.IntegerField(widget=forms.HiddenInput)
