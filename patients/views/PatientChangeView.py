from django.views import generic
# from django.urls import reverse
# from django.http import HttpResponseRedirect

from patients.admin.forms.PatientFormAdmin import PatientFormAdmin

# def redirect_patient():
#     # Generate the URL for View1
#     url = reverse('patient:patientView')
#     # Do something with the generated URL, e.g., redirect to it
#     return HttpResponseRedirect(url)


class PatientChangeView(generic.TemplateView):
    """
    Template used for our general patient page

    Template

    :template: `patient/patient.html`

    """
    template_name = "admin/patients/patient_change_form.html"
    # template_name = "patient/general_patient.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context data
        context['form'] = PatientFormAdmin()
        return context
