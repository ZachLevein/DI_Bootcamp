from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    agency = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'agency', 'password1', 'password2',)
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for fieldname in ('username', 'first_name', 'last_name',
'email', 'agency', 'password1', 'password2',):
            self.fields[fieldname].help_text = None        


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['agency']