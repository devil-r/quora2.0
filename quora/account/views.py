from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, AccountRegisterForm
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from . import view_profile
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'].lower(),
                password=form.cleaned_data['password']
            )
            login(request, user)
            request.session['alert_success'] = "Successfully logged in."
            return HttpResponseRedirect('/home')
    else:
        form = LoginForm()
    return render(request, 'tem/login.html', {'form':form})


# For allowing registration
def register_view(request):
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            view_profile.register_user(
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                form.cleaned_data['username'],
                False
            )
            #    current_site = get_current_site(request)
            #    mail_subject = 'Activate your account'
            user = authenticate(
                username=form.cleaned_data['email'].lower(),
                password=form.cleaned_data['password']
            )
            login(request, user)
            request.session['alert_success'] = "Successfully registered with the portal."

            return HttpResponseRedirect('/home')


    else:
        form = AccountRegisterForm()
    return render(request, 'tem/register.html', {'form':form})

def home_view(request):
    return render(request,'tem/home.html')
