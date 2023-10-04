from django.contrib import admin
from patients.models.AcquiredImageStatus import AcquiredImageStatus


class AcquiredImageStatusAdmin(admin.ModelAdmin):
    list_display = ("imaging_record", "radiology_staff_id", "image_status", "approval_date")
    readonly_fields = ["imaging_record"]
    search_fields = ["imaging_record__patient__name", "radiology_staff_id", "image_status"]
    fields = ("imaging_record", "radiology_staff_id", "image_status", "approval_date")

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(AcquiredImageStatus, AcquiredImageStatusAdmin)