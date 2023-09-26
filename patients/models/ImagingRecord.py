from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from utils.MyModel import MyModel
from utils.constants import EXAMINATION_REPEAT_TYPE, PATIENT_SETUP_TYPES

from patients.models.Patient import Patient

from general_setup.models.ExaminationType import ExaminationType

from facility.models.Room import Room

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class ImagingRecord(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "imaging record"
        verbose_name_plural = "imaging records"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    radiology_staff_id = models.CharField(max_length=255)
    examination_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    examination_repeat_type = models.CharField(max_length=50, choices=EXAMINATION_REPEAT_TYPE)
    examination_type = models.ManyToManyField(ExaminationType)
    setup_type = models.CharField(max_length=50, choices=PATIENT_SETUP_TYPES)
    ctdi = models.CharField(max_length=255, default='N/A')
    radiation_quality = models.CharField(max_length=255, default='N/A')
    radiation_quantity = models.CharField(max_length=255, default='N/A')
    current = models.CharField(max_length=255, default='N/A')
    radiation_time = models.TimeField(null=True)
    dose_area_product = models.CharField(max_length=255, default='N/A')
    dose_length_product = models.CharField(max_length=255, default='N/A')

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id))[0:3] + "_" + str(self.patient)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
