from django.contrib.auth.mixins import  LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site
from django.urls import reverse
from django.http import HttpResponseRedirect

from patients.models.Patient import Patient as modelHere
from patients.models.PatientNote import PatientNote
from patients.models.SpecificNote import SpecificNote

from patients.models.PatientNote import PatientNote
from patients.admin.mixins import PatientNoteMixin, ImagingRecordMixin, SpecificNoteMixin, DiagnosisMixin
from django.core import serializers

import json


class PatientDetailView(LoginRequiredMixin, PermissionRequiredMixin,  
PatientNoteMixin, SpecificNoteMixin, DiagnosisMixin, ImagingRecordMixin, DetailView):
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

        patient_notes = PatientNote.objects.filter(patient=instance).order_by('-created')
        rad_notes = SpecificNote.objects.filter(patient=instance)

        # serialized_data = serializers.serialize('json', patient_notes)

        if (patient_notes):
            general_note_instance = patient_notes.first()
            context['general_note_labels'] = general_note_instance.fields_verbose

        if (rad_notes):
            rad_note_instance = rad_notes.first()
            context['rad_note_labels'] = rad_note_instance.fields_verbose

        context['labels'] = instance.fields_verbose

        
        context['patient_notes'] = patient_notes
        context['rad_notes'] = rad_notes

        context.update(self.get_form_general_note_context())
        context.update(self.get_form_rad_note_context())
        context.update(self.get_form_diagnosis_context())
        context.update(**admin_site.each_context(self.request))
        return context

    # def get(self, request, *args, **kwargs):
    #     form_general_note = self.get_form_note()
    #     form_b = self.get_form_record()
    #     return render(request, self.template_name, {'form_general_note': form_general_note, 'form_b': form_b})

    def post(self, request, *args, **kwargs):   
        patient_pk = self.kwargs['pk']     
        patient_instance = modelHere.objects.get(pk=patient_pk)

        form_general_note = self.get_form_note()
        form_rad_note = self.get_form_rad_note()
        form_diagnosis = self.get_form_diagnosis()
        # form_b = self.get_form_record()

        if form_general_note.is_valid():            
            form_general_note.instance.patient = patient_instance
            form_general_note.instance.created_by = self.request.user
            form_general_note.save()
            return self.successUrl()

        if form_rad_note.is_valid():            
            form_rad_note.instance.patient = patient_instance
            form_rad_note.instance.created_by = self.request.user
            form_rad_note.save()
            return self.successUrl()

        if form_diagnosis.is_valid():            
            form_diagnosis.instance.patient = patient_instance
            form_diagnosis.instance.created_by = self.request.user
            form_diagnosis.save()
            return self.successUrl()

    def successUrl(self):
        patient_pk = self.kwargs['pk']     
        url = reverse("admin:patient_detail", args=[patient_pk])
        return HttpResponseRedirect(url)