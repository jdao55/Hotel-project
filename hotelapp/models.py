from django.db import models


# Create your models here.
class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    has_pool = models.BooleanField()
    has_gym = models.BooleanField()
    has_free_breakfast = models.BooleanField()
    has_restaurant = models.BooleanField()
    general_manager = models.CharField(max_length=50)
    manager_email = models.CharField(max_length=255)

    def __str__(self):
        return u'{0}, {1}\n{2}, {3}'.format(
            self.name, self.city, self.address_line1, self.address_line2)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=8)
    room_floor = models.IntegerField()
    room_type = models.CharField(max_length=20)
    has_balcony = models.BooleanField()
    room_rate_nightly = models.DecimalField(max_digits=10, decimal_places=2)
    room_rate_weekly = models.DecimalField(max_digits=10, decimal_places=2)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, to_field='hotel_id')

    def __str__(self):
        return '{0}, Room:{1} {2}'.format(
            self.room_type,
            self.room_number,
            self.room_floor,
        )


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)

    @classmethod
    def create(cls, name, email, phone_):
        customer = cls(name=name, email=email, phone=phone_)
        return customer


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    total_charges = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0.0)
    additional_charges = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0.0)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, to_field='room_id')
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, to_field='customer_id')


class ParkingLot(models.Model):
    parking_lot_id = models.AutoField(primary_key=True)
    lot_name = models.CharField(max_length=50)
    floors = models.IntegerField()
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, to_field='hotel_id')


class ParkingSpace(models.Model):
    parking_space_id = models.AutoField(primary_key=True)
    space_number = models.CharField(max_length=10)
    license_plate = models.CharField(max_length=10)
    car_make = models.CharField(max_length=20)
    parking_lot = models.ForeignKey(
        ParkingLot, on_delete=models.CASCADE, to_field='parking_lot_id')
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        to_field='customer_id',
        blank=True,
        null=True)
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        to_field='room_id',
        blank=True,
        null=True)
