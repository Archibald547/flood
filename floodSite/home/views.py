from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages

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


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("dashboard.html")
        else:
            messages.info(request, 'Disabled account')

    else:
            messages.info(request, 'Invalid login')
