from django.contrib import admin

from facility.models.Room import Room as modelHere
# from facility.models.Room import room_types_choices, examinations_choices, machines_choices
from facility.models.Machine import Machine

from utils.helpers import to_list

# from helpfuls.filters import room_type_choices, examination_choices, machine_choices

from django import forms


# room_types_choices = to_list(room_type_choices())
# examinations_choices = to_list(examination_choices())
# machines_choices = to_list(machine_choices())

class RoomFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('room_type', 'examination', 'description', 'machine')

    # room_type = forms.ChoiceField(
    #     queryset=room_types_choices,
    #     empty_label="Select Room Type",
    #     to_field_name="id",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control'
    #     })
    # )

    # examination = forms.ChoiceField(
    #     queryset=examinations_choices,
    #     empty_label="Select Examination",
    #     to_field_name="id",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control'
    #     })
    # )

    description = forms.CharField(max_length=1000, required=False,
                                  widget=forms.Textarea(attrs={
                                      'placeholder': 'Description',
                                      'class': 'form-control'
                                  }))

    # machine = forms.ModelChoiceField(
    #     queryset=machines_choices,
    #     empty_label="Select Machine",
    #     to_field_name="id",
    #     widget=forms.Select(attrs={
    #         'class': 'form-control'
    #     })
    # )


