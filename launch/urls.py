from django.urls import path
from . import views

app_name = "launch"

urlpatterns = [
    path('', views.welcome, name='welcome'),
]