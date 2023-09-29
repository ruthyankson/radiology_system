from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel

from facility.models.Machine import Machine

from django_extensions.db.models import ActivatorModel, TimeStampedModel


User = get_user_model()

class MachinePart(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "machine part"
        verbose_name_plural = "machine parts"

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    part = models.CharField(max_length=255, null=False)
    serial_number = models.CharField(max_length=255, unique=True)
    model_number = models.CharField(max_length=255, unique=True)
    date_of_manufacture = models.DateField()
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.part

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
