from patients.models.PostPreparationNote import PostPreparationNote as modelHere

from utils.constants import YES_NO

from django import forms



class PostPreparationNoteFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ("preparation_confirmation", "injection_swelling", "staff_signature", "preparation_date",)
        exclude = ("patient",)

    def __init__(self, *args, **kwargs):
        super(PostPreparationNoteFormAdmin, self).__init__(*args, **kwargs)
        self.fields['preparation_confirmation'].label = "Has patient confirmed the receival of post preparation measures?"
        self.fields['injection_swelling'].label = "Swelling at injection site?"

    
    preparation_confirmation = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO)
    
    injection_swelling = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO)
    
    staff_signature = forms.CharField(required=True, help_text="Please enter your name",
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Name',
                                          'class': 'form-control'
                                      }))

    preparation_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

   
