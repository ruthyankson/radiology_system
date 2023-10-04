import datetime
from django.contrib import admin

from patients.models.Patient import Patient as modelHere

from django import forms

from utils.constants import PATIENT_TYPES, GENDER, YES_NO, FEMALE
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field

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

    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'max': datetime.date.today()}))

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


# class PatientFormAdmin(forms.ModelForm):
    
#     def __init__(self, *args, **kwargs):
#         super(PatientFormAdmin, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_show_labels = True  # Display labels
#         self.helper.layout = Layout(
#             Field('hospital_number', placeholder='Hospital number', css_class='form-control'),
#             'patient_type',
#             Field('name', placeholder='Patient name', css_class='form-control'),
#             'date_of_birth',
#             Field('age', placeholder='Age', css_class='form-control'),
#             'gender',
#             'pregnant',
#             Field('contact', placeholder='Contact', css_class='form-control'),
#             Field('address', placeholder='Address', css_class='form-control')
#         )

#     class Meta:
#         model = modelHere
#         fields = ("hospital_number", "patient_type", "name", "date_of_birth",
#                   "age", "gender", "pregnant", "contact", "address")
    
    # ... rest of the form fields definitions remain the same


