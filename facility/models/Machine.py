from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

from utils.MyModel import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel


User = get_user_model()

class Machine(ActivatorModel, TimeStampedModel, MyModel):
    class Meta:
        verbose_name = "machine"
        verbose_name_plural = "machines"

    machine_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    machine_image = models.ImageField(null=True, blank=True, upload_to='images/')
    activate_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def image_tag(self):  # new
        return mark_safe('<img src="/../../media/%s" width="100" height="100" />' % (self.machine_image))

    def __str__(self):
        return self.machine_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
