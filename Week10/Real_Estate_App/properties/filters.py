from django.contrib.auth.models import User
import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    # price___gt = django_filters.NumberFilter(field_name='guide_price', lookup_expr='gt')
    # price__lt= django_filters.NumberFilter(field_name='guide_price', lookup_expr='lt')
    
    class Meta:
        model = Property
        fields = ['street', 'city', 'country', 'guide_price']


