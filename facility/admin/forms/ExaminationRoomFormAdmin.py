from django.contrib import admin

from facility.models.ExaminationRoom import ExaminationRoom as modelHere

from django import forms


class ExaminationRoomFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        exclude = ('deactivate_date',)
        fields = ('examination',)

    examination = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Examination',
                                          'class': 'form-control'
                                      }))


