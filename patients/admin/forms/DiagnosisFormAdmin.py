from django.contrib import admin

from patients.models.Diagnosis import Diagnosis as modelHere

from general_setup.models.ExaminationType import ExaminationType

from django import forms

from utils.constants import PATIENT_TYPES, GENDER, YES_NO

class DiagnosisFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("patient", "study_date", "ward", "requesting_physician",
                  "examination", "technique", "findings", "impressions")


    examination = forms.ModelMultipleChoiceField(queryset=ExaminationType.objects.all())

    # name = forms.CharField(max_length=255, required=True,
    #                                   widget=forms.TextInput(attrs={
    #                                       'placeholder': 'Patient name',
    #                                       'class': 'form-control'
    #                                   }))


