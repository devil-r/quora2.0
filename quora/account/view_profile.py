from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.views.generic import View
from django.template.loader import get_template
from django.shortcuts import render
from .models import Account

def register_user(email, password, user_name, active):
    user = User.objects.create_user(
        email.lower(),
        email.lower(),
        password
    )
    account = Account(
        user = user,
        username = user_name
    )
    account.save()

    return user
