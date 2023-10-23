from patients.models.ImagingRecord import ImagingRecord as modelHere, room_choices

from django import forms
from django.contrib.admin.sites import site
# from django.contrib.admin.widgets import FilteredSelectMultiple, RelatedFieldWidgetWrapper

from utils.constants import PATIENT_SETUP_TYPES, EXAMINATION_REPEAT_TYPE

from general_setup.models.ExaminationType import ExaminationType


class ImagingRecordFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("record_date", "radiology_staff_id",
                  "examination_room", "examination_repeat_type",
                  "examination_type", "setup_type", "ctdi",
                  "radiation_quality", "radiation_quantity",
                  "current", "radiation_time", "dose_area_product",
                  "dose_length_product")
        exclude = ("patient",)

    def __init__(self, *args, **kwargs):
        super(ImagingRecordFormAdmin, self).__init__(*args, **kwargs)
        self.fields['ctdi'].label = 'CTDI'
        self.fields['radiation_quality'].label = 'Radiation Quality (KVP)'
        self.fields['radiation_quantity'].label = 'Radiation Quantity (mAs)'
        self.fields['current'].label = 'Current (mA)'
        self.fields['radiation_time'].label = 'Time (sec)'
        self.fields['dose_area_product'].label = 'Dose Area Product (DAP)'
        self.fields['dose_length_product'].label = 'Dose Length Product (DLP)'

    record_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    radiology_staff_id = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')
    examination_room = forms.ChoiceField(
        choices=room_choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    
    examination_repeat_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=EXAMINATION_REPEAT_TYPE)

    examination_type = forms.ModelMultipleChoiceField(required=True, queryset=ExaminationType.objects.all(),
        widget=forms.CheckboxSelectMultiple())
    setup_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=PATIENT_SETUP_TYPES)

    ctdi = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')
    radiation_quality = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')
    radiation_quantity = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A') 
    current = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')
    radiation_time = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')
    dose_area_product = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')
    dose_length_product = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control'
                                      }), initial='N/A')

    def clean_examination_room(self):
        data = self.cleaned_data['examination_room']
        if data == "Select room":
            raise forms.ValidationError("Invalid value provided for this field.")
        return data
