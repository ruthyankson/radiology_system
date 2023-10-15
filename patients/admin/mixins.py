
from patients.models.PatientNote import PatientNote
from patients.models.ImagingRecord import ImagingRecord
from patients.models.SpecificNote import SpecificNote
from patients.models.Diagnosis import Diagnosis

from patients.admin.forms.PatientNoteFormAdmin import PatientNoteFormAdmin
from patients.admin.forms.ImagingRecordFormAdmin import ImagingRecordFormAdmin
from patients.admin.forms.SpecificNoteFormAdmin import SpecificNoteFormAdmin
from patients.admin.forms.DiagnosisFormAdmin import DiagnosisFormAdmin
from patients.admin.forms.PostPreparationNoteFormAdmin import PostPreparationNoteFormAdmin


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

class DiagnosisMixin:
    form_class_diagnosis = DiagnosisFormAdmin
    def get_form_diagnosis(self):
        return self.form_class_diagnosis(data=self.request.POST or None)
    def get_form_diagnosis_context(self):
        return {'form_diagnosis': self.get_form_diagnosis()}

class ImagingRecordMixin:
    form_class_imaging_record = ImagingRecordFormAdmin

    def get_form_record(self):
        return self.form_class_imaging_record(data=self.request.POST or None)
