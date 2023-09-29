from django.contrib import admin

from accounts.models.Profile import Profile as modelHere

from django import forms

from utils.constants import GENDER

class ProfileFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('user', 'designated_staff_id', 'title', 'job_description', 'gender', 'address', 'contact',
              'alternative_contact', 'date_of_birth', 'educational_level', 'work_experience', 'qualifications')


    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)
    qualifications = forms.CharField(max_length=1000, help_text="Please enter a qualificaton per line.",
                                      widget=forms.Textarea(attrs={
                                          'class': 'form-control'
                                      }))




