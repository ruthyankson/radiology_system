from django.db import models
from django.urls import reverse

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Job(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "job"
        verbose_name_plural = "jobs"

    job_description = models.CharField(max_length=255, unique=True)
    activate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_description

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
