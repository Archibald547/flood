from home.models import MyProfile
from django import forms
from django.forms.extras.widgets import SelectDateWidget

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ('first_name', 'last_name', 'country','birth_date','bio')
        widgets = {
            'birth_date':  SelectDateWidget()
        }
