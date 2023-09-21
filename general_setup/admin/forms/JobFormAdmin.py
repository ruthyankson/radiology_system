from django.contrib import admin

from general_setup.models.Job import Job as modelHere

from django import forms


class JobFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        exclude = ('deactivate_date',)
        fields = ('job_description',)

    job_description = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Assigned Job',
                                          'class': 'form-control'
                                      }))
