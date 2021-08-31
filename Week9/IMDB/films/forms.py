from django import forms
from .models import *
from django.forms import modelformset_factory, inlineformset_factory, widgets


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country']
        labels = {
            'country': 'Country Name'
        }



class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']
        labels = {
            'name': 'Director Name'
        }
    
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        exclude = [ 'created_by']
        widgets = {
            'name': forms.TextInput(attrs={})
        }

# AnimalFormSet = modelformset_factory(Film, form=FilmForm, extra=0)
# InlineAnimalFormSet = inlineformset_factory(Director, Film, form=FilmForm, extra=0)