from django.shortcuts import render , HttpResponse
from floodApp.forms import UserCreationForm

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

def dashboard(request):
    return render(request,'dashboard/template/dashboard.html')

def profile(request):
    return render(request,'dashboard/template/profile.html')

