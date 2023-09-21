from django.contrib import admin

from patients.models.ImagingRecord import ImagingRecord as modelHere

from django import forms

from utils.constants import PATIENT_SETUP_TYPES, EXAMINATION_REPEAT_TYPE

class ImagingRecordFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("patient", "record_date", "radiology_staff_id",
                  "examination_room", "examination_repeat_type",
                  "examination_type", "setup_type", "ctdi",
                  "radiation_quality", "radiation_quantity",
                  "current", "radiation_time", "dose_area_product",
                  "dose_length_product")

    def __init__(self, *args, **kwargs):
        super(ImagingRecordFormAdmin, self).__init__(*args, **kwargs)
        self.fields['ctdi'].label = "CTDI"

    examination_repeat_type = forms.ChoiceField(widget=forms.RadioSelect, choices=EXAMINATION_REPEAT_TYPE)

    setup_type = forms.ChoiceField(widget=forms.RadioSelect, choices=PATIENT_SETUP_TYPES)

    ctdi = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          # 'placeholder': 'N/A',
                                          # 'class': 'form-control'
                                      }), initial='N/A')

    # date_of_birth = forms.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
    #                            widget=forms.DateInput(
    #                                attrs={
    #                                    'placeholder': 'YYYY-mm-dd',
    #                                    'class': 'form-control'
    #                                }))





