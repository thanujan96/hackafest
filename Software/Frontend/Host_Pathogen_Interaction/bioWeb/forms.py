from cProfile import label
import email
from enum import unique
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            *UserCreationForm.Meta.fields,
            "first_name",
            "last_name",
            "dob",
            "username",
            "email",
            "password1",
            "password2",
            "thumb",
            "address",
        ]

    field_order = [
        "first_name",
        "last_name",
        "dob",
        "username",
        "email",
        "password1",
        "password2",
        "thumb",
        "address",
    ]

    thumb = forms.ImageField()

    address = forms.CharField(
        label="Adress", max_length=100, widget=forms.TextInput(attrs={"type": "text"})
    )

    first_name = forms.CharField(
        label="First name", min_length=3, max_length=10, required=True
    )
    last_name = forms.CharField(
        label="Last name", min_length=3, max_length=10, required=True
    )
    email = forms.EmailField(label="email")
    YEARS = [x for x in range(1940, 2021)]
    dob = forms.DateField(
        required=True,
        label="Date Of Birth",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.dob = self.cleaned_data["dob"]
        user.thumb = self.cleaned_data["thumb"]
        user.address = self.cleaned_data["address"]
        if commit:
            user.save()
        return user


class GroupsForm(forms.Form):
    groupName = forms.CharField(max_length=30)


class CSVFileFrom(forms.Form):
    groupName = forms.CharField(max_length=30)
    csvfile = forms.FileField(widget=forms.FileInput(attrs={"accept": ".csv"}))
    fileType = forms.FileField(max_length=20)
