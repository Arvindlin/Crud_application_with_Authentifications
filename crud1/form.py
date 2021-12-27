from django import forms
from django.forms import ModelForm
from .models import Information
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = ['firstname', 'lastname', 'email', 'age']


class Registration(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



