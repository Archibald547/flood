from django.shortcuts import render , HttpResponse
from floodApp.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    # username:''
    # args = {'User':username}
    return render(request, 'home/template/main.html')

def rego(request):
    if request.method =='Post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request,'home/template/rego.html', args)

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return  JsonResponse(data)

def dashboard(request):
    return render(request,'dashboard/template/dashboard.html')

def profile(request):
    return render(request,'dashboard/template/profile.html')

