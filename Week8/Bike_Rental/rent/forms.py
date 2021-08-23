from django.db import models
from django.db.models.query import QuerySet 
from .models import *
from django import forms
from django.core.exceptions import ValidationError




class add_customer(forms.Form):
    first_name = forms.CharField(max_length=50)
    second_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=30)


class add_vehicle(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())



class add_rental(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all())
