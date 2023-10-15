from patients.models.Diagnosis import Diagnosis as modelHere

from general_setup.models.ExaminationType import ExaminationType

from django import forms

from ckeditor.fields import RichTextField

class DiagnosisFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("patient", "study_date", "ward", "requesting_physician",
                  "examination", "technique", "findings", "impressions")
        exclude=("patient",)


    
    study_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    ward = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Ward',
                                          'class': 'form-control'
                                      }))
    requesting_physician = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Physician',
                                          'class': 'form-control'
                                      }))
    examination = forms.ModelMultipleChoiceField(queryset=ExaminationType.objects.all(), 
        widget=forms.CheckboxSelectMultiple())
    technique = RichTextField()
    findings = RichTextField()
    impressions = RichTextField()


