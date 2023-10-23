from django.contrib.auth.mixins import  LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from patients.models.ImagingRecord import ImagingRecord as modelHere
from patients.models.AcquiredImageStatus import AcquiredImageStatus
from patients.models.ImageRejectReasons import ImageRejectReasons
from patients.admin.mixins import ImagingStatusMixin
from patients.admin.mixins import ImageRejectReasonsMixin
from patients.models.Patient import Patient

from utils.constants import REJECTED, ACCEPTED


class ImagingRecordDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView, ImagingStatusMixin, ImageRejectReasonsMixin):
    permission_required = "patients.view_imaging_record"
    template_name = "admin/patients/imaging_record_detail.html"
    model = modelHere
    context_object_name = 'imaging_record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        imaging_record_pk = self.kwargs['pk']
        instance = modelHere.objects.get(pk=imaging_record_pk)
        admin_site: AdminSite = site
        context['title'] = 'Detail'
        context['patient'] = instance.patient
        context['labels'] = instance.fields_verbose
        context['patient_labels'] = instance.patient.fields_verbose 
        connected_docs_limit = 2

        context['labels'] = instance.fields_verbose    

        acquired_image_status_total = AcquiredImageStatus.objects.filter(imaging_record=imaging_record_pk).count()

        if acquired_image_status_total == connected_docs_limit:
            acquired_image_status = AcquiredImageStatus.objects.filter(imaging_record=imaging_record_pk).order_by('created').last()
            context['imaging_status'] = acquired_image_status
            # context['approval'] = imaging_status.approval
            context['imaging_status_labels'] = acquired_image_status.fields_verbose
            if acquired_image_status.image_status == REJECTED:
                reject_reasons_total = ImageRejectReasons.objects.filter(imaging_record=imaging_record_pk).count()
                if reject_reasons_total == connected_docs_limit:
                    reject_reasons = ImageRejectReasons.objects.filter(imaging_record=imaging_record_pk).order_by('created').last()
                    context['reject_reasons'] = reject_reasons
                    context['reject_reasons_labels'] = reject_reasons.fields_verbose
                else:
                    context['reject_reasons'] = "No data"
                    context['reject_reasons_labels'] = "No data"
            else:                
                context['reject_reasons'] = "No data"
                context['reject_reasons_labels'] = "No data"
        else:
            context['imaging_status'] = "No data"
            context['imaging_status_labels'] = "No data"

        context.update(self.get_form_imaging_status_context())
        context.update(self.get_form_reject_reasons_context())
        context.update(**admin_site.each_context(self.request))             
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        imaging_record_pk = self.kwargs['pk']
        imaging_record = modelHere.objects.get(pk=imaging_record_pk)
        patient_instance = Patient.objects.get(pk=imaging_record.patient.id)
        form_imaging_status = self.get_form_imaging_status()
        form_reject_reasons = self.get_form_reject_reasons()
        context = self.get_context_data(**kwargs) 

        if form_imaging_status.is_valid():
            if not form_imaging_status.cleaned_data['approval_date']:
                form_imaging_status.instance.approval_date = timezone.now()
            if form_imaging_status.cleaned_data['image_status'] == REJECTED:
                if form_reject_reasons.is_valid():                           
                    form_imaging_status.instance.patient = patient_instance
                    form_imaging_status.instance.imaging_record = imaging_record_pk
                    form_imaging_status.instance.radiology_staff_id = imaging_record.radiology_staff_id
                    form_imaging_status.instance.created_by = self.request.user            
                    form_reject_reasons.instance.patient = patient_instance
                    form_reject_reasons.instance.imaging_record = imaging_record_pk
                    form_reject_reasons.instance.radiology_staff_id = imaging_record.radiology_staff_id
                    form_reject_reasons.instance.created_by = self.request.user
                    form_imaging_status.save()
                    form_reject_reasons.save()
                    return self.successUrl()               
                context.update(self.get_form_reject_reasons_context())
            elif form_imaging_status.cleaned_data['image_status'] == ACCEPTED:                
                form_imaging_status.instance.patient = patient_instance
                form_imaging_status.instance.imaging_record = imaging_record_pk
                form_imaging_status.instance.radiology_staff_id = imaging_record.radiology_staff_id
                form_imaging_status.instance.created_by = self.request.user 
                form_imaging_status.save()
                return self.successUrl()
        # Handle the case where the form is not valid.
        # Re-render the detail page with the form and its errors.
        # context['form_imaging_status'] = form_imaging_status
        context.update(self.get_form_imaging_status_context())
        # return context
        return render(request, self.template_name, context)

    def successUrl(self):
        imaging_record_pk = self.kwargs['pk']     
        return HttpResponseRedirect(reverse("admin:imaging_record_detail", args=[imaging_record_pk]))

   