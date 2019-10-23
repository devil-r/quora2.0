from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class BasicForm(forms.Form):
    def disable_field(self, field):
        """
        marks field as disabled
        :param field:
        :return:
        """
        self.fields[field].widget.attrs['disabled'] = ""

    def mark_error(self, field, description):
        """
        Marks the given field as errous. The given description is displayed when the form it generated
        :param field: name of the field
        :param description: The error description
        :return:
        """
        self._errors[field] = self.error_class([description])
        del self.cleaned_data[field]

    def clear_errors(self):
        self._errors = {}

class LoginForm(BasicForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    def clean(self):
        """
        To make sure the password is valid for given email
        :return:
        """
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                self.mark_error('password', 'Incorrect Password')
        return cleaned_data

class AccountRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "UserName"
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(username=email)
        if qs.exists():
            raise forms.ValidationError("Email already registered")

        return email

    def clean(self):
        data = self.cleaned_data
        password = data['password']
        password2 = data['password2']
        if password != password2:
            raise forms.ValidationError("Password didn't match")
        return data
