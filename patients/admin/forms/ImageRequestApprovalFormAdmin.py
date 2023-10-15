from patients.models.ImageRequestApproval import ImageRequestApproval as modelHere

from django import forms

from utils.constants import IMAGE_REQUEST_APPROVAL

class ImageRequestApprovalFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("approval",)
        exclude = ("image_request",)
        
    approval = forms.ChoiceField(widget=forms.RadioSelect, choices=IMAGE_REQUEST_APPROVAL)






