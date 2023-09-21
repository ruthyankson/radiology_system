from typing import Any, Optional
from django.core.management.base import BaseCommand

from general_setup.models.RejectFactor import RejectFactor

from utilities.constants import REJECT_FACTORS
from utilities.helpers import validateUnique


class Command(BaseCommand):
    help = 'Populate Reject factor database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in REJECT_FACTORS:
            is_unique = validateUnique('general_setup.RejectFactor', 'factor', item)
            if is_unique:
                RejectFactor.objects.create(factor=item)
            else:
                self.stdout.write(self.style.ERROR('Factor already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
