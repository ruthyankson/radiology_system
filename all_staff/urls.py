from django.urls import path
from .views import custom_admin_redirect, custom_dashboard

app_name = "all_staff"

urlpatterns = [
    path('', custom_admin_redirect, name='custom_admin_redirect'),
    path('', custom_dashboard, name='custom_dashboard'),
    # ... your other URLs ...
]
