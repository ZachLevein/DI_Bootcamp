from django.db import models
from .models import  Gif_Model, Category
from django import forms


class Gif_Form(forms.Form):
    title =forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Fuck'}))
    url_link = forms.URLField(max_length=200)
    uploader_name = forms.CharField(max_length=50)
    # categories = forms.ModelChoiceField(queryset=Category.objects.all())
