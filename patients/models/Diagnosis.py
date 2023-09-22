from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from utils.MyModel import MyModel
from utils.constants import PATIENT_TYPES, GENDER, YES_NO

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from ckeditor.fields import RichTextField

from patients.models.Patient import Patient

from general_setup.models.ExaminationType import ExaminationType

class Diagnosis(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "diagnosis"
        verbose_name_plural = "diagnoses"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    study_date = models.DateTimeField()
    ward = models.CharField(max_length=255, null=True)
    requesting_physician = models.CharField(max_length=255, null=True)
    examination = models.ManyToManyField(ExaminationType)
    technique = RichTextField()
    findings = RichTextField()
    impressions = RichTextField()
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
