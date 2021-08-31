from django.db import models

# Create your models here.

class Property(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    guide_price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.CharField(max_length=2000)
    img = models.ImageField(upload_to='property')
    # agent = models.OneToOneField(User), on_delete=models.CASCADE)
    CONTRACT_CHOICES = (
        ('buy', 'buy'), 
        ('rent', 'rent'), 
        ('freehold', 'freehold')
    )
    contract_type = models.CharField(max_length=10, choices=CONTRACT_CHOICES)
    PROPERTY_CHOICES = ( 
        ('house', 'house'), 
        ('apartment', 'aparment'), 
        ('apartment', 'penthouse'),
    )
    property_type = models.CharField(max_length=10, choices=PROPERTY_CHOICES)
   
    def __str__(self):
        return f'{self.street}, {self.city}'

