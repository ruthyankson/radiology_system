from django.contrib.auth.views import LoginView
from accounts.forms.SignInForm import SignInForm

from utils.constants import APP_NAME

# from admin_argon.forms import LoginForm


# def redirect_sign_in():
#     # Generate the URL for View1
#     url = reverse('accounts:SignInView')
#     # Do something with the generated URL, e.g., redirect to it
#     return HttpResponseRedirect(url)



class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'
    form_class = SignInForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context data
        context['app_name'] = APP_NAME
        return context

