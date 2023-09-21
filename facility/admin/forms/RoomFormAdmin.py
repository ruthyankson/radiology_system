from django.contrib import admin

from facility.models.Room import Room as modelHere
from facility.models.Machine import Machine
from facility.models.ExaminationRoom import ExaminationRoom
from facility.models.RoomType import RoomType

from django import forms


class RoomFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        fields = ('room_type', 'examination', 'description', 'machine')

    room_type = forms.ModelChoiceField(
        queryset=RoomType.objects.all(),
        empty_label="Select Room Type",
        to_field_name="id",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    examination = forms.ModelChoiceField(
        queryset=ExaminationRoom.objects.all(),
        empty_label="Select Examination",
        to_field_name="id",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    description = forms.CharField(max_length=1000, required=False,
                                  widget=forms.Textarea(attrs={
                                      'placeholder': 'Description',
                                      'class': 'form-control'
                                  }))

    machine = forms.ModelChoiceField(
        queryset=Machine.objects.all(),
        empty_label="Select Machine",
        to_field_name="id",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )


