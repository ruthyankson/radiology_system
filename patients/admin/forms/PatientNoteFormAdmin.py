
from patients.models.PatientNote import PatientNote as modelHere


from ckeditor.fields import RichTextField

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

    note = RichTextField()

    note_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

   
