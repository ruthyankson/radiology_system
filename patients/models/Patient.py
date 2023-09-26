from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from utils.MyModel import MyModel
from utils.constants import PATIENT_TYPES, GENDER, YES_NO

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Patient(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"

    hospital_number = models.CharField(max_length=255)
    patient_type = models.CharField(max_length=50, choices=PATIENT_TYPES)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    pregnant = models.CharField(max_length=50, choices=YES_NO, null=True, blank=True)
    contact = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id))[0:5] + " " + self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
