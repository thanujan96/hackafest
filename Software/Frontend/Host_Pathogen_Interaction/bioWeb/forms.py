from enum import unique
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class GroupsForm(forms.Form):
    groupName = forms.CharField(max_length=30)


class CSVFileFrom(forms.Form):
    groupName = forms.CharField(max_length=30)
    csvfile = forms.FileField(widget=forms.FileInput(attrs={"accept": ".csv"}))
