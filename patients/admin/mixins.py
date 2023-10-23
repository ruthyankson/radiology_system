
import logging
# from patients.models.PatientNote import PatientNote
# from patients.models.ImagingRecord import ImagingRecord
# from patients.models.SpecificNote import SpecificNote
# from patients.models.Diagnosis import Diagnosis
from patients.models.ImageRequestApproval import ImageRequestApproval

from patients.admin.forms.PatientNoteFormAdmin import PatientNoteFormAdmin
from patients.admin.forms.ImagingRecordFormAdmin import ImagingRecordFormAdmin
from patients.admin.forms.SpecificNoteFormAdmin import SpecificNoteFormAdmin
from patients.admin.forms.DiagnosisFormAdmin import DiagnosisFormAdmin
from patients.admin.forms.ImageRequestFormAdmin import ImageRequestFormAdmin
from patients.admin.forms.ImageRequestApprovalFormAdmin import ImageRequestApprovalFormAdmin
from patients.admin.forms.AcquiredImageStatusFormAdmin import AcquiredImageStatusFormAdmin
from patients.admin.forms.ImageRejectReasonsFormAdmin import ImageRejectReasonsFormAdmin
from patients.admin.forms.PostPreparationNoteFormAdmin import PostPreparationNoteFormAdmin


logger = logging.getLogger(__name__)

class PatientNoteMixin:
    form_class_note = PatientNoteFormAdmin
    def get_form_note(self):
        return self.form_class_note(data=self.request.POST or None)
    # def get_patient_notes(self):
    #     return PatientNote.objects.all()
    def get_form_general_note_context(self):
        context = {
            'form_general_note': self.get_form_note(),
            # 'patient_notes': self.get_patient_notes()
        }
        return context

class SpecificNoteMixin:
    form_class_rad_note = SpecificNoteFormAdmin
    def get_form_rad_note(self):
        return self.form_class_rad_note(data=self.request.POST or None)
    def get_form_rad_note_context(self):
        return {'form_rad_note': self.get_form_rad_note()}

class PostPreparationMixin:
    form_class_post_preparation = PostPreparationNoteFormAdmin
    def get_form_post_preparation(self):
        return self.form_class_post_preparation(data=self.request.POST or None)
    def get_form_post_preparation_context(self):
        return {'form_post_preparation': self.get_form_post_preparation()}

class DiagnosisMixin:
    form_class_diagnosis = DiagnosisFormAdmin
    def get_form_diagnosis(self):
        return self.form_class_diagnosis(data=self.request.POST or None)
    def get_form_diagnosis_context(self):
        return {'form_diagnosis': self.get_form_diagnosis()}

class ImageRequestMixin:
    form_class_image_request = ImageRequestFormAdmin
    def get_form_image_request(self):
        return self.form_class_image_request(data=self.request.POST or None)
    def get_form_image_request_context(self):
        return {'form_image_request': self.get_form_image_request()}
        

class ImageRequestApprovalMixin:
    form_class_image_request_approval = ImageRequestApprovalFormAdmin
    def get_form_image_request_approval(self, request_key):
        if request_key:
            try:
                instanceHere = ImageRequestApproval.objects.get(image_request=request_key)
            except ImageRequestApproval.DoesNotExist:
                instanceHere = None
        else:
            instanceHere = None
        return self.form_class_image_request_approval(data=self.request.POST or None, instance=instanceHere)
    def get_form_image_request_approval_context(self, rk):
        return {'form_image_request_approval': self.get_form_image_request_approval(request_key=rk)}

class ImagingRecordMixin:
    form_class_imaging_record = ImagingRecordFormAdmin
    def get_form_imaging_record(self):
        return self.form_class_imaging_record(data=self.request.POST or None)
    def get_form_imaging_record_context(self):
        return {'form_imaging_record': self.get_form_imaging_record()}

class ImagingStatusMixin:
    form_class_imaging_status = AcquiredImageStatusFormAdmin
    def get_form_imaging_status(self):
        return self.form_class_imaging_status(data=self.request.POST or None)
    def get_form_imaging_status_context(self):
        return {'form_imaging_status': self.get_form_imaging_status()}

class ImageRejectReasonsMixin:
    form_class_image_reject_reasons = ImageRejectReasonsFormAdmin
    def get_form_reject_reasons(self):
        return self.form_class_image_reject_reasons(data=self.request.POST or None)
    def get_form_reject_reasons_context(self):
        return {'form_reject_reasons': self.get_form_reject_reasons()}

