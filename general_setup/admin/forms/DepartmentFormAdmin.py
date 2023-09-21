from django.contrib import admin

from general_setup.models.Department import Department as modelHere

from django import forms


class DepartmentFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('department_name',)
        exclude = ('deactivate_date',)

    department_name = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Department',
                                   'class': 'form-control'
                               }))





