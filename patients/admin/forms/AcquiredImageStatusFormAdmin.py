from patients.models.AcquiredImageStatus import AcquiredImageStatus as modelHere

from django import forms

from utils.constants import ACQUIRED_IMAGE_STATUS

class AcquiredImageStatusFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("approval_date", "radiology_staff_id", "image_status",)
        exclude = ("patient", "imaging_record",)
        

    approval_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}), required=False)
    radiology_staff_id = forms.CharField(max_length=255, required=False,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'ID',
                                   'class': 'form-control'
                               }))
    image_status = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=ACQUIRED_IMAGE_STATUS)








