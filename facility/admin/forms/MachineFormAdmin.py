from django.contrib import admin

from facility.models.Machine import Machine as modelHere

from django import forms


class MachineFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        exclude = ('deactivate_date',)
        fields = ('machine_name', 'description', 'machine_image')

    machine_name = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Machine',
                                          'class': 'form-control'
                                      }))

    description = forms.CharField(max_length=1000, required=False,
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Description',
                                  'class': 'form-control'
                              }))


