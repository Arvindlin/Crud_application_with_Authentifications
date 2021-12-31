from django import forms
from django.forms import ModelForm, Form
from .models import Information
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class InformationForm(Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput())
    age = forms.IntegerField()

    def get_query_set(self):
        model = Information
        return model

    def save(self, context):
        model = self.get_query_set()
        data = self.cleaned_data
        instance = model.objects.create(user=context.user, **data)
        instance.save()
        return instance


class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
