from django.contrib import admin

from facility.models.RoomType import RoomType as modelHere

from django import forms


class RoomTypeFormAdmin(forms.ModelForm):
    class Meta:
        model = modelHere
        exclude = ('deactivate_date',)
        fields = ('type_of_room',)

    type_of_room = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={
                                          'placeholder': 'Type of Room',
                                          'class': 'form-control'
                                      }))


