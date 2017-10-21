from registration.forms import RegistrationFormUniqueEmail
from django import forms
# from django.forms import Textarea
from .models import MyProfile
from django.forms.extras.widgets import SelectDateWidget
# from django.forms import TextArea


class ProfileForm(RegistrationFormUniqueEmail):
    model = MyProfile
    # fields = {'first_name', 'last_name', 'loaction'}
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30, required = False)
    birth_date = forms.DateField(widget=SelectDateWidget, required = False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}), required = False)
    # widgets = {
    #     'birth_date' : forms.DateInput(),
    # }

