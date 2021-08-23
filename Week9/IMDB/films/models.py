from django.db import models
import datetime

class Country(models.Model):
    country = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.country}'

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.category_name}'

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.date.today)
    # created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_country = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField("Director")
    def __str__(self):
            return f'{self.title}'

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
            return f'{self.first_name} {self.last_name}'

