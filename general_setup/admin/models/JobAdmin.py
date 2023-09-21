from django.contrib import admin
from general_setup.models.Job import Job
from general_setup.admin.forms.JobFormAdmin import JobFormAdmin


class JobAdmin(admin.ModelAdmin):
    list_display = ('job_description',)
    form = JobFormAdmin
    search_fields = ['job_description']

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Job, JobAdmin)
