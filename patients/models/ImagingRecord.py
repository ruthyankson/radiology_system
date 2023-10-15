from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel
from utils.constants import EXAMINATION_REPEAT_TYPE, PATIENT_SETUP_TYPES, ACQUIRED_IMAGE_STATUS
from utils.helpers import to_list

from patients.models.Patient import Patient

from general_setup.models.ExaminationType import ExaminationType

from facility.models.Room import Room

from django_extensions.db.models import ActivatorModel, TimeStampedModel



def imaging_rooms():
    return [(item.examination, item.room_type + " " + item.examination) for item in Room.objects.all()]

User = get_user_model()
room_choices = [("Select Procedure", "Select Procedure"),]
room_choices += to_list(imaging_rooms())

class ImagingRecord(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "imaging record"
        verbose_name_plural = "imaging records"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    radiology_staff_id = models.CharField(max_length=255)
    examination_room =  models.CharField(max_length=100, choices=room_choices)
    examination_repeat_type = models.CharField(max_length=50, choices=EXAMINATION_REPEAT_TYPE)
    examination_type = models.ManyToManyField(ExaminationType)
    image_status = models.CharField(max_length=50, choices=ACQUIRED_IMAGE_STATUS)
    setup_type = models.CharField(max_length=50, choices=PATIENT_SETUP_TYPES)
    ctdi = models.CharField(max_length=255, default='N/A', verbose_name='CTDI')
    radiation_quality = models.CharField(max_length=255, default='N/A', verbose_name='Radiation Quality (KVP)')
    radiation_quantity = models.CharField(max_length=255, default='N/A', verbose_name='Radiation Quantity (mAs)')
    current = models.CharField(max_length=255, default='N/A', verbose_name='Current (mA)')
    radiation_time = models.DurationField(null=True, verbose_name='Time (sec)')
    dose_area_product = models.CharField(max_length=255, default='N/A', verbose_name='Dose Area Product (DAP)')
    dose_length_product = models.CharField(max_length=255, default='N/A', verbose_name='Dose Length Product (DLP)')

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id))[0:3] + "_" + str(self.patient)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
