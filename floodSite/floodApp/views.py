from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/main.html')

def rego(request):
    return render(request,'home/register.html')


