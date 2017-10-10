from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class home(TemplateView):
	template_name = "home.html"

class privacy_policy(TemplateView):
    template_name = "privacy_policy.html"
               