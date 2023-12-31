from typing import Any, Optional
from django.core.management.base import BaseCommand

from general_setup.models.ExaminationType import ExaminationType

from utils.constants import EXAMINATION_TYPES
from utils.helpers import validateUnique


class Command(BaseCommand):
    help = 'Populate Examination type database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in EXAMINATION_TYPES:
            is_unique = validateUnique('general_setup.ExaminationType', 'type_name', item)
            if is_unique:
                ExaminationType.objects.create(type_name=item, created_by=User.objects.get(pk=1))
            else:
                self.stdout.write(self.style.ERROR('Examination type already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
