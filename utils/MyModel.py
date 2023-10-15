# Python imports
import uuid

# Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyModel(models.Model):
    '''
    used in every db entry
    '''

    id = models.UUIDField(
        _('id'),
        primary_key=True,
        default=uuid.uuid4
        )
    
    class Meta:
        abstract = True

    @property
    def fields_verbose(self):
        return dict([ (f.name, f.verbose_name) for f in self._meta.fields + self._meta.many_to_many ])

