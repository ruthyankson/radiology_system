from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.Patient import Patient


User = get_user_model()

class SpecificNote(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "specific note"
        verbose_name_plural = "specific notes"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.FloatField()
    type_of_procedure = models.CharField(max_length=255)
    pre_procedure_bp = models.CharField(max_length=255)
    pulse = models.CharField(max_length=255)
    start_time_of_exams = models.TimeField(auto_now=True)
    end_time_of_exams = models.TimeField(auto_now=True)
    volume_of_contrast = models.CharField(max_length=255)
    flow_rate = models.CharField(max_length=255)
    post_procedure_bp = models.CharField(max_length=255)
    post_pulse = models.CharField(max_length=255)
    general_comments = models.TextField(max_length=500)
    note_date = models.DateTimeField(auto_now=True, verbose_name="date")
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " " + "specific note " + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
