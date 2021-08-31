from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [   
    path('profile/', views.UpdateProfile.as_view(), name='profile'),
]