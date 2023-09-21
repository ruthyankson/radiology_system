from django.contrib import admin

from general_setup.models.Holiday import Holiday as modelHere

from django import forms


class HolidayFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('day_name', 'day_date',)

    day_name = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Day Name',
                                   'class': 'form-control'
                               }))

    day_date = forms.DateField(required=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                               widget=forms.DateInput(
                                   attrs={
                                       'placeholder': 'YYYY-mm-dd',
                                       'class': 'form-control'
                                   }))





