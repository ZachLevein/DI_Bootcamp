from django.db import models

from rent.models import *
from faker import Faker


fake=Faker()
fake.add_provider(VehicleProvider)


for i in range(10):
    first = fake.first_name()
    last = fake.last_name()
    email = fake.ascii_email()
    phone = fake.phone_number()
    Customer.objects.create(first_name=first, second_name=last, email=email, phone_number=phone)

fake.vehicle_make_model()

from django.db import models

from rent.models import *
from faker import Faker
from faker_vehicle import VehicleProvider

fake=Faker()
fake.add_provider(VehicleProvider)

# Creating Vehicle data 
for i in range(100):
    make = fake.vehicle_make_model()
    type= fake.vehicle_category()
    VehicleType.objects.create(name=make)

for i in range(10):
    type= fake.vehicle_category()
    VehicleSize.objects.create(size=type)


# Generating Fake Dates
from rent.models import *
from faker import Faker
import datetime

fake=Faker()

for i in range(5):
    rental = fake.past_date(start_date='-150d', tzinfo=None)
    returning = fake.past_date(start_date='-40d', tzinfo=None)
    print(returning)
    Rental.objects.create(rental_date=rental, return_date=returning)



#Finding Unique values in the SIZE model
for i in VehicleSize.objects.order_by().values('size').distinct():
    pair = i 
    for values in pair.values(): 
        print(values)