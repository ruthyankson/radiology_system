from django.contrib import admin

from patients.models.Patient import Patient as modelHere

from django import forms

from utils.constants import PATIENT_TYPES, GENDER, YES_NO

class PatientFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("hospital_number", "patient_type", "name", "date_of_birth",
                  "age", "gender", "pregnant", "contact", "address")

    hospital_number = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Hospital number',
                                   'class': 'form-control'
                               }))

    patient_type = forms.ChoiceField(widget=forms.RadioSelect, choices=PATIENT_TYPES)

    name = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Patient name',
                                          'class': 'form-control'
                                      }))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
                                          'placeholder': 'Age',
                                          'class': 'form-control'
                                      }))

    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)

    pregnant = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO, required=False)

    contact = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Contact',
                                          'class': 'form-control'
                                      }))

    address = forms.CharField(max_length=255,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Address',
                                          'class': 'form-control'
                                      }))

    # def show_pregnant(self):




