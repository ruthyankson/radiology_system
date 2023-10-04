from django.contrib import admin
from general_setup.models.Job import Job
from general_setup.admin.forms.JobFormAdmin import JobFormAdmin
from django.contrib.sites.models import Site

# Unregister the Site model from the default admin site
admin.site.unregister(Site)


class JobAdmin(admin.ModelAdmin):
    list_display = ('job_description',)
    form = JobFormAdmin
    search_fields = ['job_description']

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(Job, JobAdmin)
