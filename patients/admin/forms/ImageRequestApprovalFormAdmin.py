from django.contrib import admin

from patients.models.ImageRequestApproval import ImageRequestApproval as modelHere

from django import forms

from utils.constants import IMAGE_REQUEST_APPROVAL

class ImageRequestApprovalFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("image_request", "approval")

    hospital_number = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Image Request',
                                   'class': 'form-control'
                               }))


    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=IMAGE_REQUEST_APPROVAL)






