from django import forms
from django.db.models.query_utils import select_related_descend
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [ 
            'street', 
            'city', 
            'country', 
            'zip', 
            'guide_price', 
            'bedrooms', 
            'bathrooms', 
            'description',
            'img',
            'contract_type', 
            'property_type'
        ]
