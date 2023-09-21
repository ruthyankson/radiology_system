from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from utils.MyModel import MyModel
from utils.constants import ACQUIRED_IMAGE_STATUS

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.ImagingRecord import ImagingRecord

class AcquiredImageStatus(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "acquired image status"
        verbose_name_plural = "acquired images statuses"

    imaging_record = models.ForeignKey(ImagingRecord, on_delete=models.CASCADE)
    approval_date = models.DateTimeField(null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    radiology_staff_id = models.CharField(max_length=255)
    image_status = models.CharField(max_length=50, choices=ACQUIRED_IMAGE_STATUS)
    
    activate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.imaging_record)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
