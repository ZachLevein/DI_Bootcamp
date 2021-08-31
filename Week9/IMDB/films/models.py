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

class Director(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.date.today)
    # available_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default="")

    def __str__(self):
            return f'{self.title}'


