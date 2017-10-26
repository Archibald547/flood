from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required(login_url='/accounts/login/')
def dashboard(request):
	return render(request,'dashboard.html')



# Create your views here.

class profile(TemplateView):
	template_name = "profile.html"

class reset_password(TemplateView):
	template_name = "change_password.html"
#
# class update_profile(TemplateView):
# 	template_name = "update_profile.html"

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance=request.user.myprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('update_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        profile_form = UpdateProfileForm(instance=request.user.myprofile)
    return render(request, 'update_profile.html', {
        'profile_form': profile_form
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/change_password/done/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'password_form': password_form
    })

@login_required
def change_password_done(request):
	return render(request,'change_password_done.html')
