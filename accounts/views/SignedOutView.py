from django.views import generic


# def redirect_signed_out():
#     # Generate the URL for View1
#     url = reverse('account:SignedOutView')
#     # Do something with the generated URL, e.g., redirect to it
#     return HttpResponseRedirect(url)


class SignedOutView(generic.TemplateView):

    template_name = 'accounts/signed-out.html'

