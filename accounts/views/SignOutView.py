from accounts.views.SignedOutView import SignedOutView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
# from django.contrib.auth import logout

def redirect_sign_out():
    # Generate the URL for View1
    url = reverse('account:SignOutView')
    # Do something with the generated URL, e.g., redirect to it
    return HttpResponseRedirect(url)


class SignOutView(LogoutView):
    next_page = reverse_lazy('accounts:signed_out')  # Replace with your custom logged-out view name
