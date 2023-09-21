from typing import Any, Optional
from django.core.management.base import BaseCommand

from general_setup.models.Department import Department as modelHere

from utils.constants import DEPARTMENTS
from utils.helpers import validateUnique


class Command(BaseCommand):
    help = 'Populate Department database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in DEPARTMENTS:
            is_unique = validateUnique('general_setup.Department', 'department_name', item)
            if is_unique:
                modelHere.objects.create(department_name=item)
            else:
                self.stdout.write(self.style.ERROR('Department already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
