from django.db import models
from django.urls import reverse


# Create your models here.
class Booking(models.Model):
    # user = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    active = models.BooleanField(default=False, editable=True)


# class Booked(models.Model):
#     active = models.BooleanField(default=False, editable=True)


    # def get_absolute_url(self):
    #     return reverse("booking:booking_detail", kwargs={"id": self.id})