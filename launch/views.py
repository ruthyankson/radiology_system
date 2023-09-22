from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def redirect_welcome():
  # Generate the URL for View1
  url = reverse('launch:welcome')
  # Do something with the generated URL, e.g., redirect to it
  return HttpResponseRedirect(url)

def welcome(request):
  return render(request, 'pages/welcome.html')


