from django.contrib import admin

from patients.models.PatientNote import PatientNote as modelHere

from ckeditor.widgets import CKEditorWidget

# from datetimepicker.widgets import DateTimePicker

from django import forms



class PatientNoteFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("note_title", "note", "note_date")
        exclude = ("patient",)

    note_title = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Title',
                                   'class': 'form-control'
                               }))

    note = forms.CharField(widget=CKEditorWidget())

    note_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

   
