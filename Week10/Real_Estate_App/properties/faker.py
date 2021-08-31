from django.db import *
from faker import Faker
from random import randint

fake = Faker()
fake.add_provider(BaseProvider)


for i in range(8):
    street = fake.street_address()
    city = fake.city()
    country = fake.country()
    zip = fake.postcode()
    bathrooms = randint(1, 7)
    bedrooms = bathrooms * 2
    guide_price = randint(50000, 3000000)



#Code to iniatlize objects 

from properties.models import Property
from faker import Faker
from random import randint
fake = Faker()

description = "lorem, ortico's are absolutely delighted to offer for sale this well presented end of terrace Victorian family home to the market. The property is an excellent purchase for first time buyers looking for a home suitable for the family looking for excellent living and entertaining space"

for i in range(8):
    street = fake.street_address()
    city = fake.city()
    country = fake.country()
    zip = fake.postcode()
    bathrooms = randint(1, 7)
    bedrooms = bathrooms * 2
    guide_price = randint(50000, 3000000)
    Property.objects.create(street=street, city=city, country=country, zip=zip, guide_price=guide_price, bedrooms=bedrooms, bathrooms=bathrooms, description=description, img="65815_WER012054000_IMG_01_0001.jpeg", contract_type='buy', property_type='house')

