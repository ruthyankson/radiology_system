from django.shortcuts import render

from utils.constants import APP_NAME

def error_404_view(request, exception=None):
    return render(request, 'extraneous/error404.html', status=404)

def extraneous_base(request):
  app_name = APP_NAME
  context = {'app_name': app_name}
  return render(request, 'layouts/ext_base.html', context)
