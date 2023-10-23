from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from facility.models.ExaminationRoom import ExaminationRoom as modelHere

from utils.constants import EXAMINATIONS
from utils.helpers import validateUnique


User = get_user_model()

class Command(BaseCommand):
    help = 'Populate Examination Room database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in EXAMINATIONS:
            is_unique = validateUnique('facility.ExaminationRoom', 'examination', item)
            if is_unique:
                modelHere.objects.create(examination=item, created_by=User.objects.get(pk=1))
            else:
                self.stdout.write(self.style.ERROR('Examination already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
