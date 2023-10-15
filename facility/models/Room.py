from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel
from utils.helpers import to_list

# from helpfuls.filters import room_type_choices, examination_choices, machine_choices

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from facility.models.ExaminationRoom import ExaminationRoom
from facility.models.RoomType import RoomType
from facility.models.Machine import Machine


def examination_choices():
    return [(item.examination, item.examination) for item in ExaminationRoom.objects.all()]


def room_type_choices():
    return [(item.type_of_room, item.type_of_room) for item in RoomType.objects.all()]


def machine_choices():
    return [(item.machine_name, item.machine_name) for item in Machine.objects.all()]

User = get_user_model()
room_types_choices = to_list(room_type_choices())
examinations_choices = to_list(examination_choices())
machines_choices = to_list(machine_choices())

class Room(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"

    room_type = models.CharField(max_length=255, choices=room_types_choices)
    examination = models.CharField(max_length=255, choices=examinations_choices)
    description = models.TextField(max_length=500, blank=True)
    machine = models.CharField(max_length=255, choices=machines_choices)
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return str(self.examination)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


