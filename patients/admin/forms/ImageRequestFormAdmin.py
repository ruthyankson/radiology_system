# from django.contrib import admin
#
# # from patients.models.ImageRequest import ImageRequest as modelHere
#
# from django import forms
#
# class ImageRequestFormAdmin(forms.Form):
#     class Meta:
#         # model = modelHere
#         fields = ("patient", "patient_age", "gender", "address",
#                   "request_date", "ward", "brief_clinical_history",
#                   "radiological_investigation_requested",
#                   "medical_officer", "station",
#                   "radiology_serial_number", "previous_exams_details",)
#
#     hospital_number = forms.CharField(max_length=255, required=True,
#                                widget=forms.TextInput(attrs={
#                                    'placeholder': 'Hospital number',
#                                    'class': 'form-control'
#                                }))
#
#     patient_type = forms.ChoiceField(widget=forms.RadioSelect, choices=PATIENT_TYPES)
#
#     name = forms.CharField(max_length=255, required=True,
#                                       widget=forms.TextInput(attrs={
#                                           'placeholder': 'Patient name',
#                                           'class': 'form-control'
#                                       }))
#
#     # date_of_birth = forms.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
#     #                            widget=forms.DateInput(
#     #                                attrs={
#     #                                    'placeholder': 'YYYY-mm-dd',
#     #                                    'class': 'form-control'
#     #                                }))
#
#     age = forms.IntegerField(widget=forms.NumberInput(attrs={
#                                           'placeholder': 'Age',
#                                           'class': 'form-control'
#                                       }))
#
#     gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)
#
#     pregnant = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO)
#
#     contact = forms.CharField(max_length=255, required=True,
#                                       widget=forms.TextInput(attrs={
#                                           'placeholder': 'Contact',
#                                           'class': 'form-control'
#                                       }))
#
#     address = forms.CharField(max_length=255,
#                                       widget=forms.TextInput(attrs={
#                                           'placeholder': 'Address',
#                                           'class': 'form-control'
#                                       }))
#
#
