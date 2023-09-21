from django.contrib import admin

from django import forms

from general_setup.models.RejectFactor import RejectFactor as modelHere


class RejectFactorFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        exclude = ('deactivate_date',)
        fields = ('factor',)

    factor = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Factor',
                                          'class': 'form-control'
                                      }))
