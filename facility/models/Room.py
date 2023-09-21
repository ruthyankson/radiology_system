from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from facility.models.RoomType import RoomType
from facility.models.Machine import Machine
from facility.models.ExaminationRoom import ExaminationRoom


class Room(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"

    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    examination = models.ForeignKey(ExaminationRoom, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    activate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.examination

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
