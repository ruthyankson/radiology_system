from typing import Any, Optional
from django.core.management.base import BaseCommand

from general_setup.models.Job import Job

from utils.constants import JOBS
from utils.helpers import validateUnique


class Command(BaseCommand):
    help = 'Populate Job database with some jobs'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for job in JOBS:
            is_unique = validateUnique('general_setup.Job', 'job_description', job)
            if is_unique:
                Job.objects.create(job_description=job, created_by=User.objects.get(pk=1))
            else:
                self.stdout.write(self.style.ERROR('Job description already exists'))
        return self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
