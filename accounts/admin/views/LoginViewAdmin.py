from django.contrib.auth.views import LoginView

from utils.constants import APP_NAME
# from django.http import HttpResponseRedirect

# from accounts.admin.forms.LoginFormAdmin import LoginFormAdmin


# def redirect_sign_in():
#     # Generate the URL for View1
#     url = reverse('accounts:LoginViewAdmin')
#     # Do something with the generated URL, e.g., redirect to it
#     return HttpResponseRedirect(url)


class LoginViewAdmin(LoginView):
    template_name = 'admin/login.html'
    # form_class = LoginFormAdmin

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context data
        context['app_name'] = APP_NAME
        return context

