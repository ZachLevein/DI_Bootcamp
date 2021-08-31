from accounts.models import Profile
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def signup_view(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.agency = form.cleaned_data.get('agency')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        return render(request, 'accounts/profile.html', {'form': form})

    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})


class UpdateProfile(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = EditUserForm(instance=self.request.user)
        return context
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def form_valid(self, form):
        user_form = EditUserForm(self.request.POST, instance=self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)


# @login_required
# def profile_view(request):
#     url = request.user.profile.url


# class UpdateProfile(LoginRequiredMixin, UpdateView):
#     form_class = EditProfileForm
#     template_name = 'accounts/profile.html'
#     success_url = reverse_lazy('profile')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = EditUserForm(instance=self.request.user)
#         return context

#     def get_object(self, queryset=None):
#         return self.request.user.profile

#     def form_valid(self, form):
#         user_form = EditUserForm(self.request.POST, instance=self.request.user)
#         if user_form.is_valid():
#             user_form.save()
#         return super().form_valid(form)