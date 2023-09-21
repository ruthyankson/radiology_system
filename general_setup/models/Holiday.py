from django.db import models
from django.urls import reverse

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Holiday(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "holiday"
        verbose_name_plural = "holidays"

    day_name = models.CharField(max_length=255, unique=True)
    day_date = models.DateField()
    activate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.day_name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
