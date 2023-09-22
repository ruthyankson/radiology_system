from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from utils.MyModel import MyModel
from utils.constants import PATIENT_TYPES, GENDER, YES_NO

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from ckeditor.fields import RichTextField

from patients.models.Patient import Patient

class PatientNote(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "patient note"
        verbose_name_plural = "patient notes"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note_date = models.DateTimeField()
    note_title = models.CharField(max_length=255, null=True)
    note = RichTextField()
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
