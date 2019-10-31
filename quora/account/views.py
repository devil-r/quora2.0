from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, AccountRegisterForm
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from . import view_profile
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == 'POST':
        if "username" not in request.POST:
            user = authenticate(
                username=request.POST.get('email','something').lower(),
                password=request.POST.get('password','')
            )
            if user is None:
                return render(request, 'login.html')
            login(request,user)
            request.session['alert_success'] = "Successfully logged in."

            return redirect('/home')
        else:
            
            view_profile.register_user(
                request.POST['email'],
                request.POST['password'],
                request.POST['username'],
                False
            )
            #    current_site = get_current_site(request)
            #    mail_subject = 'Activate your account'
            user = authenticate(
                username=request.POST['email'].lower(),
                password=request.POST['password']
            )

            return HttpResponseRedirect('/')

    return render(request, 'login.html')
