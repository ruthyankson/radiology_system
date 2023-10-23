from patients.models.SpecificNote import SpecificNote as modelHere, procedure_choices

# from datetimepicker.widgets import DateTimePicker

from django import forms



class SpecificNoteFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("weight", "type_of_procedure", "pre_procedure_bp_systolic", "pre_procedure_bp_diastolic", "pre_pulse",
        "start_time_of_exams", "end_time_of_exams", "volume_of_contrast", "flow_rate", "post_procedure_bp_systolic",
        "post_procedure_bp_diastolic", "post_pulse", "general_comments", "note_date")
        exclude = ("patient",)

    weight = forms.FloatField(widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'number',
                                   'step': '0.001'
                               }))
    type_of_procedure = forms.ChoiceField(
        choices=procedure_choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    pre_procedure_bp_systolic = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    pre_procedure_bp_diastolic = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    pre_pulse = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    
    start_time_of_exams = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    end_time_of_exams = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

    volume_of_contrast = forms.FloatField(widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'number',
                                   'step': '0.001'
                               }))
    flow_rate = forms.FloatField(widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'number',
                                   'step': '0.001'
                               }))
    
    
    post_procedure_bp_systolic = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    post_procedure_bp_diastolic = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    post_pulse = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    
    general_comments = forms.CharField(max_length=1000, required=False, 
    widget=forms.Textarea(attrs={'placeholder': 'Comments',
                                   'class': 'form-control'}))

    note_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

    def clean_type_of_procedure(self):
        val = self.cleaned_data['type_of_procedure']
        if val == "Select Procedure":
            raise forms.ValidationError("Please select a procedure.")
        return val
   
