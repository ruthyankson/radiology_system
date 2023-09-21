from django.contrib import admin

from general_setup.models.ExaminationType import ExaminationType as modelHere

from django import forms


class ExaminationTypeFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('type_name',)
        exclude = ('deactivate_date',)

    type_name = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Type',
                                   'class': 'form-control'
                               }))





