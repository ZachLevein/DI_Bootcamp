from django.shortcuts import redirect, render
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Profile
from django.contrib.auth import authenticate, login





class UserCreation(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def register(self, form):
        profile_form =ProfileForm(self.request.POST)
        if profile_form.is_valid():
            new_user = form.save()
            print(form.cleaned_data)
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            user = authenticate(username=['username'], password=['password1'])
            print(user)
            if user:
                login(self.request, user)
                print('You are logged in')
            return redirect('home')
        else:
            return self.form_invalid(form)

class MyLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
