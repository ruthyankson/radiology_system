from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.Patient import Patient


User = get_user_model()

class ImageRequest(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "image request"
        verbose_name_plural = "image requests"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    request_date = models.DateTimeField()
    ward = models.CharField(max_length=255, null=True)
    brief_clinical_history = models.TextField(max_length=500)
    radiological_investigation_requested = models.TextField(max_length=500)
    medical_officer = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255)
    radiology_serial_number = models.CharField(max_length=255)
    previous_exams_details = models.TextField(max_length=500)

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " image request " + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
