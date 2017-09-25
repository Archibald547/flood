from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/template/main.html')

def rego(request):
    return render(request,'home/template/register.html')

def dashboard(request):
    return render(request,'dashboard/template/dashboard.html')

def profile(request):
    return render(request,'dashboard/template/profile.html')

