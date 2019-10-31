from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Answer

class Answer_handler(forms.Form):
    ans_text = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":20}))
    is_anonymous = forms.BooleanField(required=True,initial=False)

    class Meta:
        model = Answer
