from django.shortcuts import render , HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyProfile
from .serializers import ProfileSerializer
from django.views.generic import TemplateView



# from floodApp.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


class privacy_policy(TemplateView):
    template_name = "privacy_policy.html"

def password_reset(request):
    return render(request,'registration/password_reset_form.html')
