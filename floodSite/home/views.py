from django.shortcuts import render , HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from home.forms import ProfileForm

# from floodApp.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


class privacy_policy(TemplateView):
    template_name = "privacy_policy.html"

