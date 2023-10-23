from patients.models.ImageRequest import ImageRequest as modelHere

from django import forms

class ImageRequestFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("request_date", "ward", "brief_clinical_history",
                  "radiological_investigation_requested",
                  "medical_officer", "department",
                  "radiology_serial_number", "previous_exams_details",)
        exclude = ("patient",)

    request_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    ward = forms.CharField(max_length=255, required=False,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Ward',
                                   'class': 'form-control'
                               }))
    brief_clinical_history = forms.CharField(max_length=1000, required=True, 
    widget=forms.Textarea(attrs={'placeholder': 'Clinical history',
                                   'class': 'form-control'}))
    radiological_investigation_requested = forms.CharField(max_length=1000, required=True, 
    widget=forms.Textarea(attrs={'placeholder': 'Requested radiological investigation',
                                   'class': 'form-control'}))
    medical_officer = forms.CharField(max_length=255, required=False,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Medical officer',
                                   'class': 'form-control'
                               }))
    department = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Department',
                                   'class': 'form-control'
                               }))
    radiology_serial_number = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Radiology serial number',
                                   'class': 'form-control'
                               }))
    previous_exams_details = forms.CharField(max_length=1000, required=True, 
    widget=forms.Textarea(attrs={'placeholder': 'Previous exams details',
                                   'class': 'form-control'}))

   