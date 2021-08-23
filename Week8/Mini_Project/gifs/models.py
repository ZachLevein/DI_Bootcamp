from django.db import models
from django.db.models.fields import CharField


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Gif_Model(models.Model):
    title = models.CharField(max_length=50)
    url_link = models.URLField(max_length=200)
    uploader_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    # categories = models.ManyToManyField(Category)


    def __str__(self):
        return f'Gif_Model: {self.title}'

