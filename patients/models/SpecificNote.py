from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from utils.MyModel import MyModel
from utils.helpers import to_list

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.Patient import Patient

from general_setup.models.ExaminationType import ExaminationType


def procedures():
    return [(item.type_name, item.type_name) for item in ExaminationType.objects.all()]

User = get_user_model()
procedure_choices = [("Select Procedure", "Select Procedure"),]
procedure_choices += to_list(procedures())

class SpecificNote(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "radiology note"
        verbose_name_plural = "radiology notes"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.FloatField()
    type_of_procedure = models.CharField(max_length=50, choices=procedure_choices)
    pre_procedure_bp_systolic = models.IntegerField(verbose_name="Pre Procedure BP (Systolic [mm Hg])")
    pre_procedure_bp_diastolic = models.IntegerField(verbose_name="Pre Procedure BP (Diastolic [mm Hg])")
    pre_pulse = models.IntegerField(verbose_name="Pulse (bpm)")
    start_time_of_exams = models.TimeField(default=timezone.now)
    end_time_of_exams = models.TimeField(default=timezone.now)
    volume_of_contrast = models.FloatField(verbose_name="Volume of Contrast (mL)")
    flow_rate = models.FloatField(verbose_name="Flow Rate (mL/s)")
    post_procedure_bp_systolic = models.IntegerField(verbose_name="Post Procedure BP (Systolic [mm Hg])")
    post_procedure_bp_diastolic = models.IntegerField(verbose_name="Post Procedure BP (Diastolic [mm Hg])")
    post_pulse = models.IntegerField(verbose_name="Post Pulse (bpm)")
    general_comments = models.TextField(max_length=500)
    note_date = models.DateTimeField(verbose_name="date", default=timezone.now)
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " radiology note " + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
