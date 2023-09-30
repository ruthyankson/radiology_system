from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from utils.constants import APP_NAME

# Create your views here.

app_name = APP_NAME

def redirect_welcome():
  # Generate the URL for View1
  url = reverse('launch:welcome')
  # Do something with the generated URL, e.g., redirect to it
  return HttpResponseRedirect(url)

def welcome_view(request):
  context = {'app_name': app_name}
  return render(request, 'pages/welcome.html', context)

def main_base_view(request):
  context = {'app_name': app_name}
  return render(request, 'layouts/main_base.html', context)

def base_view(request):
  context = {'app_name': app_name}
  return render(request, 'layouts/base.html', context)


