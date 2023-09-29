from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from general_setup.models.EducationalLevel import EducationalLevel

from utils.constants import EDUCATIONAL_LEVELS
from utils.helpers import validateUnique

from helpfuls.filters import User


User = get_user_model()

class Command(BaseCommand):
    help = 'Populate Educational level database'

    # @receiver(post_save, sender=userHere)
    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in EDUCATIONAL_LEVELS:
            is_unique = validateUnique('general_setup.EducationalLevel', 'level', item)
            if is_unique:
                EducationalLevel.objects.create(level=item, created_by=User.objects.get(pk=1))
            else:
                self.stdout.write(self.style.ERROR('Educational level already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))


    # def create_user_profile(sender, instance, created, **kwargs):
    #     print("Sender --> ", sender)
    #     print("Instance -->", instance)
    #     print("Created --> ", created)
    #     if created:
    #         Profile.objects.create(user=instance)
