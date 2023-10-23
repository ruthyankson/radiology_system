from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from utils.MyModel import MyModel
from utils.constants import ACQUIRED_IMAGE_STATUS

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.Patient import Patient


User = get_user_model()

class AcquiredImageStatus(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "acquired image status"
        verbose_name_plural = "acquired images statuses"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    imaging_record = models.UUIDField()
    approval_date = models.DateTimeField(default=timezone.now)
    radiology_staff_id = models.CharField(max_length=255, null=True)
    image_status = models.CharField(max_length=50, choices=ACQUIRED_IMAGE_STATUS)
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " imaging status "  + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
