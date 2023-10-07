from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel
from utils.constants import YES_NO

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from ckeditor.fields import RichTextField

from patients.models.Patient import Patient


User = get_user_model()

class PatientPostPreparationNote(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "patient post preparation note"
        verbose_name_plural = "patient post preparation notes"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    preparation_confirmation = models.CharField(max_length=50, choices=YES_NO)
    injection_swelling = models.CharField(max_length=50, choices=YES_NO)
    staff_signature = models.CharField(max_length=255)
    preparation_date = models.DateTimeField(auto_now=True)
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
