from registration.forms import RegistrationFormUniqueEmail
from django import forms
# from django.forms import Textarea
from .models import MyProfile
from django.forms.extras.widgets import SelectDateWidget
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User
from django_countries import widgets, countries

# from django.forms import TextArea


class ProfileForm(RegistrationFormUniqueEmail):
    model = MyProfile

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    country = forms.ChoiceField(widget=CountrySelectWidget, choices=countries)
    birth_date = forms.DateField(widget=SelectDateWidget, required = False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}), required = False)

