from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel

from ckeditor.fields import RichTextField

from patients.models.Patient import Patient


User = get_user_model()

class PatientNote(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "patient note"
        verbose_name_plural = "patient notes"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=255, null=True, verbose_name='title')
    note = RichTextField()
    note_date = models.DateTimeField(verbose_name="date", default=timezone.now)
    
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient)

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

    # @property
    # def fields_verbose(self):
    #     return dict([ (f.name, f.verbose_name) for f in self._meta.fields + self._meta.many_to_many ])

