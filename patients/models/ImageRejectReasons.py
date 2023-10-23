from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel
from utils.constants import ACQUIRED_IMAGE_STATUS

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.Patient import Patient

from general_setup.models.RejectFactor import RejectFactor
from general_setup.models.RejectSubFactor import RejectSubFactor


User = get_user_model()

class ImageRejectReasons(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "image reject reason"
        verbose_name_plural = "image reject reasons"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    imaging_record = models.UUIDField()
    radiology_staff_id = models.CharField(max_length=255)
    factors = models.ManyToManyField(RejectFactor)
    sub_factors = models.ManyToManyField(RejectSubFactor)

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.patient) + " reject reason "  + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
