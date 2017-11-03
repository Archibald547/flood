from django import forms
from .models import todo

class PostForm(forms.ModelForm):

    class Meta:
        model = todo
        fields = ('name', 'description', 'date',)