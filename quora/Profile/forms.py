from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class Edit_info(forms.Form):
    address = forms.CharField()
    age = forms.IntegerField(required = True)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}) , help_text="Give a little description about yourself")
    education = forms.CharField()
    class Meta:
        model = Account
        #fields = ['gender',]
