from patients.models.ImageRejectReasons import ImageRejectReasons as modelHere

from django import forms

from utils.constants import ACQUIRED_IMAGE_STATUS

from general_setup.models.RejectFactor import RejectFactor
from general_setup.models.RejectSubFactor import RejectSubFactor

class ImageRejectReasonsFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("factors", "sub_factors",)
        exclude = ("patient", "imaging_record", "radiology_staff_id",)        

    # radiology_staff_id = forms.CharField(max_length=255, required=False,
    #                            widget=forms.TextInput(attrs={
    #                                'placeholder': 'ID',
    #                                'class': 'form-control'
    #                            }))

    factors = forms.ModelMultipleChoiceField(required=False, queryset=RejectFactor.objects.all(), 
    help_text="Please hold down the 'Ctrl or Command' key to select multiple factors",
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    sub_factors = forms.ModelMultipleChoiceField(required=False, queryset=RejectSubFactor.objects.all(), 
    help_text="Please hold down the 'Ctrl' or 'Command' key to select multiple sub-factors",
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))








