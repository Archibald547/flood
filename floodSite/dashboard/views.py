from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def dashboard(request):
	return render(request,'dashboard.html')



# Create your views here.

class profile(TemplateView):
	template_name = "profile.html"

class update_profile(TemplateView):
	template_name = "update_profile.html"
