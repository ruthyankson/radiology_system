from typing import Any, Optional
from django.core.management.base import BaseCommand

from general_setup.models.EducationalLevel import EducationalLevel

from utilities.constants import EDUCATIONAL_LEVELS
from utilities.helpers import validateUnique


class Command(BaseCommand):
    help = 'Populate Educational level database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in EDUCATIONAL_LEVELS:
            is_unique = validateUnique('general_setup.EducationalLevel', 'level', item)
            if is_unique:
                EducationalLevel.objects.create(level=item)
            else:
                self.stdout.write(self.style.ERROR('Educational level already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
