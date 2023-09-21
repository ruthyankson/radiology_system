from typing import Any, Optional
from django.core.management.base import BaseCommand

from general_setup.models.RejectSubFactor import RejectSubFactor

from utils.constants import REJECT_SUB_FACTORS
from utils.helpers import validateUnique


class Command(BaseCommand):
    help = 'Populate Reject sub factor database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in REJECT_SUB_FACTORS:
            is_unique = validateUnique('general_setup.RejectSubFactor', 'sub_factor', item)
            if is_unique:
                RejectSubFactor.objects.create(sub_factor=item)
            else:
                self.stdout.write(self.style.ERROR('Sub factor already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
