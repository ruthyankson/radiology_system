from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from accounts.forms.SignInForm import SignInForm

# from admin_argon.forms import LoginForm


def redirect_sign_in():
    # Generate the URL for View1
    url = reverse('accounts:SignInView')
    # Do something with the generated URL, e.g., redirect to it
    return HttpResponseRedirect(url)



class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'
    form_class = SignInForm

