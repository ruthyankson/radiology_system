from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from ckeditor.fields import RichTextField

from patients.models.Patient import Patient

from general_setup.models.ExaminationType import ExaminationType


User = get_user_model()

class Diagnosis(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "diagnosis"
        verbose_name_plural = "diagnoses"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    study_date = models.DateTimeField(default=timezone.now)
    ward = models.CharField(max_length=255, null=True)
    requesting_physician = models.CharField(max_length=255, null=True)
    examination = models.ManyToManyField(ExaminationType)
    technique = RichTextField()
    findings = RichTextField()
    impressions = RichTextField()
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " diagnosis "  + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
