from django.contrib import admin

from general_setup.models.EducationalLevel import EducationalLevel as modelHere

from django import forms


class EducationalLevelFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('level',)
        exclude = ('deactivate_date',)

    level = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Level',
                                   'class': 'form-control'
                               }))





