from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class SignInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))