from django.db import models
from django.urls import reverse

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class RejectSubFactor(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "reject sub factor"
        verbose_name_plural = "reject sub factors"

    sub_factor = models.CharField(max_length=255, unique=True)
    activate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_factor

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
