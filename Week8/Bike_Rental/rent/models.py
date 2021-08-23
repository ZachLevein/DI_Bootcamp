from typing import Sized
from django.db import models
from django.db.models.fields import *

class Customer(models.Model):
    # customer_id = models.Field(primary_key=True, blank=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    # class Address(models.Model):
    #     street = models.TextField()
    #     city = models.TextField()
    #     country= models.TextField()

        

    def __str__(self):
        return f'{self.first_name}, {self.second_name},'


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    real_cost = models.IntegerField(null=True)
    size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE)  
    def __str__(self):
        return f'{self.vehicle_type}, {self.size}'


class VehicleType(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.name}'

class VehicleSize(models.Model):
    size = models.CharField(max_length= 50)
    def __str__(self):
        return f'{self.size}'

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(default=None)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Customer: {self.customer} Vehicle: {self.vehicle}'
 

class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.PROTECT)
    size = models.ForeignKey("VehicleSize", on_delete=models.PROTECT)
   

   