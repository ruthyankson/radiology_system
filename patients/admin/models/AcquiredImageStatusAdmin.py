from django.contrib import admin
from patients.models.AcquiredImageStatus import AcquiredImageStatus


class AcquiredImageStatusAdmin(admin.ModelAdmin):
    list_display = ("imaging_record", "radiology_staff_id", "image_status", "approval_date")
    search_fields = ["imaging_record", "radiology_staff_id", "image_status"]
    fields = ("imaging_record", "radiology_staff_id", "image_status", "approval_date")

admin.site.register(AcquiredImageStatus, AcquiredImageStatusAdmin)