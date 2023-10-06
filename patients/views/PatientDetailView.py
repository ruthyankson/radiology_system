from django.views import generic



class PatientDetailView(generic.TemplateView):
    """
    Template used for our general patient page

    Template

    :template: `patient/patient.html`

    """
    template_name = "admin/patients/patient_detail.html"
    # template_name = "patient/general_patient.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Add custom context data
    #     context['form'] = PatientFormAdmin()
    #     return context