from django.contrib import admin

from facility.models.MachinePart import MachinePart as modelHere
from facility.models.Machine import Machine

from django import forms


class MachinePartFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('machine', 'part', 'serial_number', 'model_number', 'date_of_manufacture')

    machine = forms.ModelChoiceField(
        queryset=Machine.objects.all(),
        empty_label="Select Machine",
        to_field_name="id",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    part = forms.CharField(max_length=255, required=True,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Part',
                                  'class': 'form-control'
                              }))

    serial_number = forms.CharField(max_length=255, required=True,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Serial Number',
                               'class': 'form-control'
                           }))

    model_number = forms.CharField(max_length=255,
                                    widget=forms.TextInput(attrs={
                                        'placeholder': 'Model Number',
                                        'class': 'form-control'
                                    }))

    date_of_manufacture = forms.DateField(required=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                               widget=forms.DateInput(
                                   attrs={
                                       'placeholder': 'YYYY-mm-dd',
                                       'class': 'form-control'
                                   }))


