from accounts.models import Profile
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import SignupForm, EditUserForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
