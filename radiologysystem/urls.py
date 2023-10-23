"""
URL configuration for radiologysystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls import handler404

from utils.constants import APP_NAME, APP_NAME_URL, APP_ROOT_URL


# Django admin header customization

admin.site.site_header = APP_NAME
# admin.site.site_title = APP_NAME
# admin.site.index_title = APP_NAME + " Administration"

urlpatterns = [
    path(f'{APP_ROOT_URL}/', include('launch.urls')),
    path(f'{APP_ROOT_URL}/{APP_NAME_URL}/', admin.site.urls),
    path(f'{APP_ROOT_URL}/{APP_NAME_URL}/staff/', include('all_staff.urls')),
    path(f'{APP_ROOT_URL}/{APP_NAME_URL}/patients/', include('patients.urls')),
    path(f'{APP_ROOT_URL}/{APP_NAME_URL}/task_assignment/', include('task_assignment.urls')),
    path(f'{APP_ROOT_URL}/{APP_NAME_URL}/reject_analysis/', include('reject_analysis.urls')),
    path(f'{APP_ROOT_URL}/{APP_NAME_URL}/accounts/', include('accounts.urls')),

    path('general_setup/', include('general_setup.urls')),
    path('facility/', include('facility.urls')),

    
    # path("__debug__/", include("debug_toolbar.urls")),
]


# if not settings.PRODUCTION:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = 'extraneous.views.error_404_view'
