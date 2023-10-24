from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from utils.MyModel import MyModel
from utils.constants import YES_NO

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from patients.models.Patient import Patient


User = get_user_model()

class PostPreparationNote(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "post preparation note"
        verbose_name_plural = "post preparation notes"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    preparation_confirmation = models.CharField(max_length=3, choices=YES_NO, 
        verbose_name="Has patient confirmed the receival of post preparation measures?")
    injection_swelling = models.CharField(max_length=3, choices=YES_NO, verbose_name="Swelling at injection site?")
    staff_signature = models.CharField(max_length=255)
    preparation_date = models.DateTimeField(verbose_name="date", default=timezone.now)
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient) + " post preparation " + (str(self.id))[0:3]

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
