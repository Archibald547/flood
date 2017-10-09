from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
# from floodApp.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.http import JsonResponse

# Create your views here.
def home(request):
    # username:''
    # args = {'User':username}
    return render(request, 'home.html')


class privacy_policy(TemplateView):
    template_name = "privacy_policy.html"
