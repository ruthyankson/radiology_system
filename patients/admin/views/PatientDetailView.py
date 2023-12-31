from django.contrib.auth.mixins import  LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render

from patients.models.Patient import Patient as modelHere
from patients.models.PatientNote import PatientNote
from patients.models.SpecificNote import SpecificNote
from patients.models.Diagnosis import Diagnosis
from patients.models.ImageRequest import ImageRequest
from patients.models.ImageRequestApproval import ImageRequestApproval
from patients.models.ImagingRecord import ImagingRecord
from patients.models.AcquiredImageStatus import AcquiredImageStatus
from patients.models.ImageRejectReasons import ImageRejectReasons
from patients.models.PostPreparationNote import PostPreparationNote

from patients.models.PatientNote import PatientNote
from patients.admin.mixins import PatientNoteMixin, ImagingRecordMixin, ImageRejectReasonsMixin, SpecificNoteMixin, DiagnosisMixin, PostPreparationMixin, ImageRequestMixin, ImageRequestApprovalMixin, ImagingStatusMixin

from utils.constants import ACCEPTED, REJECTED, NO_DATA

class PatientDetailView(LoginRequiredMixin, PermissionRequiredMixin, ImageRequestApprovalMixin, 
PatientNoteMixin, SpecificNoteMixin, DiagnosisMixin, ImageRequestMixin, PostPreparationMixin,
ImagingRecordMixin, ImageRejectReasonsMixin, ImagingStatusMixin, DetailView):
    permission_required = "patients.view_patient"
    template_name = "admin/patients/patient_detail.html"
    model = modelHere
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_pk = self.kwargs['pk']
        admin_site: AdminSite = site
        # data = modelHere.objects.all()
        form_invalid = False
        context['form_invalid'] = form_invalid
        context['title'] = 'Detail'
        instance = modelHere.objects.get(pk=patient_pk)

        # serialized_data = serializers.serialize('json', patient_notes)

        if (instance):            
            context['labels'] = instance.fields_verbose     

            patient_notes = PatientNote.objects.filter(patient=instance).order_by('-created')
            rad_notes = SpecificNote.objects.filter(patient=instance).order_by('-created')
            diagnoses = Diagnosis.objects.filter(patient=instance).order_by('-created')
            image_requests = ImageRequest.objects.filter(patient=instance).order_by('-created')
            # image_request_approvals = ImageRequestApproval.objects.filter(patient=instance).order_by('-created')
            imaging_records = ImagingRecord.objects.filter(patient=instance).order_by('-created')
            # imaging_statuses = AcquiredImageStatus.objects.filter(patient=instance).order_by('-created')
            image_reject_reasons = ImageRejectReasons.objects.filter(patient=instance).order_by('-created')
            post_preparation_notes = PostPreparationNote.objects.filter(patient=instance).order_by('-created')

        if (patient_notes):
            context['patient_notes'] = patient_notes
            general_note_instance = patient_notes.first()
            context['general_note_labels'] = general_note_instance.fields_verbose
        else:
            context['general_note_labels'] = NO_DATA
            context['patient_notes'] = NO_DATA

        if (rad_notes):
            context['rad_notes'] = rad_notes
            rad_note_instance = rad_notes.first()
            context['rad_note_labels'] = rad_note_instance.fields_verbose
        else:
            context['rad_note_labels'] = NO_DATA
            context['rad_notes'] = NO_DATA

        if (diagnoses):
            context['diagnoses'] = diagnoses
            diagnosis_instance = diagnoses.first()
            context['diagnosis_labels'] = diagnosis_instance.fields_verbose
        else:
            context['diagnosis_labels'] = NO_DATA
            context['diagnoses'] = NO_DATA

        if (image_requests):
            context['image_requests'] = image_requests
            image_request_instance = image_requests.first()
            context['image_request_labels'] = image_request_instance.fields_verbose
        else:
            context['image_request_labels'] = NO_DATA
            context['image_requests'] = NO_DATA

        if (imaging_records):
            context['imaging_records'] = imaging_records
            imaging_record_instance = imaging_records.first()
            context['imaging_record_labels'] = imaging_record_instance.fields_verbose            
        else:
            context['imaging_record_labels'] = NO_DATA
            context['imaging_records'] = NO_DATA

        if (image_reject_reasons):
            context['image_reject_reasons'] = image_reject_reasons
            image_reject_reasons_instance = image_reject_reasons.first()
            context['image_reject_reasons_labels'] = image_reject_reasons_instance.fields_verbose            
        else:
            context['image_reject_reasons_labels'] = NO_DATA
            context['image_reject_reasons'] = NO_DATA

        if (post_preparation_notes):
            context['post_preparation_notes'] = post_preparation_notes
            post_preparation_instance = post_preparation_notes.first()
            context['post_preparation_labels'] = post_preparation_instance.fields_verbose
        else:
            context['post_preparation_labels'] = NO_DATA
            context['post_preparation_notes'] = NO_DATA
        
        
       
        
        
        
        
        context['ajax_url'] = self.ajaxUrl()

        context.update(self.get_form_general_note_context())
        context.update(self.get_form_rad_note_context())
        context.update(self.get_form_diagnosis_context())
        context.update(self.get_form_image_request_context())
        context.update(self.get_form_imaging_record_context())
        context.update(self.get_form_post_preparation_context())
        context.update(self.get_form_reject_reasons_context())
        context.update(self.get_form_imaging_status_context())
        context.update(**admin_site.each_context(self.request))
        return context

    # def get(self, request, *args, **kwargs):
    #     form_general_note = self.get_form_note()
    #     form_b = self.get_form_record()
    #     return render(request, self.template_name, {'form_general_note': form_general_note, 'form_b': form_b})

    # show_modal = False

    def post(self, request, *args, **kwargs): 
        self.object = self.get_object()  
        patient_pk = self.kwargs['pk']     
        patient_instance = modelHere.objects.get(pk=patient_pk)
        context = self.get_context_data(**kwargs) 
        # form_invalid = False

        form_general_note = self.get_form_note()
        form_rad_note = self.get_form_rad_note()
        form_diagnosis = self.get_form_diagnosis()
        form_image_request = self.get_form_image_request()
        form_imaging_record = self.get_form_imaging_record()
        form_post_preparation = self.get_form_post_preparation()
        form_reject_reasons = self.get_form_reject_reasons()
        form_imaging_status = self.get_form_imaging_status()


        if form_general_note.is_valid():            
            form_general_note.instance.patient = patient_instance
            form_general_note.instance.created_by = self.request.user
            form_general_note.full_clean()
            form_general_note.save()
            return self.successUrl()           
        form_invalid = True
        context['form_invalid'] = form_invalid 
        context['form_general_note'] = form_general_note
        context.update(self.get_form_general_note_context())

        if form_rad_note.is_valid():            
            form_rad_note.instance.patient = patient_instance
            form_rad_note.instance.created_by = self.request.user
            form_rad_note.full_clean()
            form_rad_note.save()
            return self.successUrl()           
        form_invalid = True
        context['form_invalid'] = form_invalid 
        context['form_rad_note'] = form_rad_note
        context.update(self.get_form_rad_note_context())

        if form_diagnosis.is_valid():            
            form_diagnosis.instance.patient = patient_instance
            form_diagnosis.instance.created_by = self.request.user
            form_diagnosis.full_clean()
            form_diagnosis.save()
            return self.successUrl()         
        form_invalid = True
        context['form_invalid'] = form_invalid 
        context['form_diagnosis'] = form_diagnosis
        context.update(self.get_form_diagnosis_context())

        if form_image_request.is_valid():            
            form_image_request.instance.patient = patient_instance
            form_image_request.instance.created_by = self.request.user
            ImageRequestApproval.objects.create(patient=patient_instance, image_request=form_image_request.instance.id, created_by=self.request.user)
            form_image_request.full_clean()
            form_image_request.save()
            return self.successUrl()
        form_invalid = True
        context['form_invalid'] = form_invalid 
        context['form_image_request'] = form_image_request
        context.update(self.get_form_image_request_context())
       
        if form_imaging_status.is_valid():
            if form_imaging_status.instance.image_status == ACCEPTED:  
                if form_imaging_record.is_valid():                           
                    form_imaging_record.instance.patient = patient_instance
                    form_imaging_record.instance.created_by = self.request.user 
                    form_imaging_status.instance.patient = patient_instance
                    form_imaging_status.instance.imaging_record = form_imaging_record.instance.id
                    form_imaging_status.instance.radiology_staff_id = form_imaging_record.instance.radiology_staff_id
                    form_imaging_status.instance.created_by = self.request.user 
                    form_imaging_status.full_clean()  
                    form_imaging_record.full_clean()
                    form_imaging_status.save()
                    form_imaging_record.save()
                    return self.successUrl()  
                form_invalid = True
                context['form_invalid'] = form_invalid 
                context['form_imaging_record'] = form_imaging_record              
                context.update(self.get_form_imaging_record_context())
            elif form_imaging_status.instance.image_status == REJECTED:
                if form_imaging_record.is_valid():
                    if form_reject_reasons.is_valid():                              
                        form_imaging_record.instance.patient = patient_instance
                        form_imaging_record.instance.created_by = self.request.user        
                        form_imaging_status.instance.patient = patient_instance
                        form_imaging_status.instance.imaging_record = form_imaging_record.instance.id
                        form_imaging_status.instance.radiology_staff_id = form_imaging_record.instance.radiology_staff_id
                        form_imaging_status.instance.created_by = self.request.user            
                        form_reject_reasons.instance.patient = patient_instance
                        form_reject_reasons.instance.imaging_record = form_imaging_record.instance.id
                        form_reject_reasons.instance.radiology_staff_id = form_imaging_record.instance.radiology_staff_id
                        form_reject_reasons.instance.created_by = self.request.user
                        form_imaging_status.full_clean()  
                        form_imaging_record.full_clean()
                        form_reject_reasons.full_clean()
                        form_imaging_status.save()
                        form_imaging_record.save()
                        form_reject_reasons.save()
                        return self.successUrl()    
                    form_invalid = True
                    context['form_invalid'] = form_invalid   
                    context['form_reject_reasons'] = form_imaging_record               
                    context.update(self.get_form_reject_reasons_context())   
                form_invalid = True
                context['form_invalid'] = form_invalid       
                context['form_imaging_record'] = form_imaging_record        
                context.update(self.get_form_imaging_record_context())
        form_invalid = True
        context['form_invalid'] = form_invalid 
        context['form_imaging_status'] = form_imaging_status 
        context.update(self.get_form_imaging_status_context())
            
        if form_post_preparation.is_valid():            
            form_post_preparation.instance.patient = patient_instance
            form_post_preparation.instance.created_by = self.request.user
            form_post_preparation.full_clean()
            form_post_preparation.save()
            return self.successUrl()
        form_invalid = True
        context['form_invalid'] = form_invalid 
        context['form_post_preparation'] = form_post_preparation
        context.update(self.get_form_post_preparation_context())
        # context[''] = 
        # return context
        return render(request, self.template_name, context)

    def successUrl(self):
        patient_pk = self.kwargs['pk']     
        url = reverse("admin:patient_detail", args=[patient_pk])
        return HttpResponseRedirect(url)

    def ajaxUrl(self):
        patient_pk = self.kwargs['pk']     
        url = reverse("admin:patient_detail", args=[patient_pk])
        return url

    # def showRejectReasons(self, request, *args, **kwargs):
    #     # email = request.POST.get('email')
        
    #     # imaging_records = ImagingRecord.objects.filter(patient=instance).order_by('-created')
    #     return