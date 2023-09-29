from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel
from utils.constants import TASK_STATUS
# from utils.helpers import to_list
# from helpfuls.filters import room_choices, assigned_staff_choices, machine_choices
from helpfuls.helpful_lists import staff_choices, rooms_choices, dept_choices

from django_extensions.db.models import ActivatorModel, TimeStampedModel


User = get_user_model()

class Task(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    deadline = models.DateTimeField()
    title = models.CharField(max_length=255)
    task = models.TextField(max_length=500)
    assigned_staff = models.CharField(max_length=255, choices=staff_choices)
    room = models.CharField(max_length=255, choices=rooms_choices, null=True, blank=True)
    department = models.CharField(max_length=255, choices=dept_choices, null=True, blank=True)
    status = models.CharField(max_length=255, choices=TASK_STATUS)

    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
