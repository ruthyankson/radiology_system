from django.urls import include, path

from accounts.views.SignInView import SignInView
from django.contrib.auth import views as auth_views

from accounts.admin.forms.LoginFormAdmin import LoginFormAdmin
from accounts.views.SignedOutView import SignedOutView
from accounts.views.SignOutView import SignOutView
from accounts.admin.views.LoginViewAdmin import LoginViewAdmin

app_name = "accounts"

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('admin/login', LoginViewAdmin.as_view(), name="admin_login"),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('signed-out/', SignedOutView.as_view(), name='signed_out'),
    path('sign-out/', SignOutView.as_view(), name='sign_out'),

]
