from django.contrib import admin

from django import forms

from general_setup.models.RejectSubFactor import RejectSubFactor as modelHere


class RejectSubFactorFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        exclude = ('deactivate_date',)
        fields = ('sub_factor',)

    sub_factor = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Sub-factor',
                                          'class': 'form-control'
                                      }))
