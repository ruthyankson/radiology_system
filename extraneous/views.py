from django.shortcuts import render

def error_404_view(request, exception=None):
    return render(request, 'extraneous/error404.html', status=404)
