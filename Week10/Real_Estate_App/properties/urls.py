from django.contrib import admin
from django.urls import include, path
from. import views
from .filters import *




urlpatterns=[
        path('home', views.HomePage.as_view(), name='home'),
        path('property/list', views.PropertyListView.as_view(), name='property_list'),
        path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
        path('property/search', views.PropertySearch, name='property_search'),

]