from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel
from utils.constants import IMAGE_REQUEST_APPROVAL

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.ImageRequest import ImageRequest
from patients.models.Patient import Patient


User = get_user_model()

class ImageRequestApproval(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "image request approval"
        verbose_name_plural = "image request approvals"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image_request = models.UUIDField()
    approval = models.CharField(max_length=50, choices=IMAGE_REQUEST_APPROVAL, null=True)

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " image request approval " + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
