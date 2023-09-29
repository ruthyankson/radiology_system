from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel


User = get_user_model()

class RoomType(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "room type"
        verbose_name_plural = "room types"

    type_of_room = models.CharField(max_length=255, unique=True)
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_of_room

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
