from django.db import models
from django.urls import reverse
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

# from general_setup.models.Job import Job
# from general_setup.models.EducationalLevel import EducationalLevel

from utils.MyModel import MyModel
from utils.constants import GENDER, WORK_EXPERIENCE, EDUCATIONAL_LEVELS
from utils.helpers import to_list

from helpfuls.filters import edu_level_choices, job_choices


from django_extensions.db.models import ActivatorModel, TimeStampedModel


User = get_user_model()
job_des_choices = to_list(job_choices())
educational_level_choices = to_list(edu_level_choices())

class Profile(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designated_staff_id = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.CharField(max_length=50, choices=job_des_choices, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    alternative_contact = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    educational_level = models.CharField(max_length=60, choices=educational_level_choices, null=True, blank=True)
    work_experience = models.CharField(max_length=255, choices=WORK_EXPERIENCE, null=True, blank=True)
    qualifications = models.TextField(null=True, blank=True)

    activate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
