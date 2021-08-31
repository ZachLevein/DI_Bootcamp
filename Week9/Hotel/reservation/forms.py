from django import forms
from django.db.models.query_utils import select_related_descend
from .models import * 

import datetime 
from datetime import date
from calendar import monthrange

# class BookingForm(forms.Form):
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)
#     check_in = forms.DateField()
#     check_out = forms.DateField()

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 
            'first_name', 
            'last_name', 
            'check_in', 
            'check_out'
        ]


    