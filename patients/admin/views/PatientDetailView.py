from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site

from patients.models.Patient import Patient as modelHere


class PatientDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "patients.view_patient"
    template_name = "admin/patients/patient_detail.html"
    model = modelHere

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_object_name = 'patient'
        patient_pk = self.kwargs['pk']
        admin_site: AdminSite = site
        data = modelHere.objects.all()
        context['data'] = data
        context['title'] = 'Detail'
        instance = modelHere.objects.get(pk=patient_pk)
        context['labels'] = instance.fields_verbose
        key_verbose_value_pairs = {(field.name, field.verbose_name): getattr(instance, field.name) for field in modelHere._meta.fields}
        # context['labels'] = key_verbose_value_pairs
        # context['some_key'] = 'Some data based on PK: ' + str(self.kwargs['pk'])
        context.update(**admin_site.each_context(self.request))
        # context['form'] = modelHere.objects.filter()
        return context