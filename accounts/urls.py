from django.urls import include, path

from accounts.views.SignInView import SignInView
# from extraneous.views.ErrorPageView import ErrorPageView
from django.contrib.auth import views as auth_views
from accounts.views.SignedOutView import SignedOutView
from accounts.views.SignOutView import SignOutView


app_name = "accounts"

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('signed-out/', SignedOutView.as_view(), name='signed_out'),
    path('sign-out/', SignOutView.as_view(), name='sign_out'),

]
