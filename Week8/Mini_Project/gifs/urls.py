from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='index' ),
    path('admin/', views.admin, name='admin' ),
    path('add_form/', views.add_form, name='add_form')
]