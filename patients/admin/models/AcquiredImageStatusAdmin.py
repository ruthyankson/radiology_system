from django.contrib import admin
from patients.models.AcquiredImageStatus import AcquiredImageStatus


class AcquiredImageStatusAdmin(admin.ModelAdmin):
    list_display = ("patient", "radiology_staff_id", "image_status", "approval_date")
    readonly_fields = ["patient"]
    search_fields = ["patient__name", "radiology_staff_id", "image_status"]
    fields = ("radiology_staff_id", "image_status", "approval_date")
    ordering = ("-created",)

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(AcquiredImageStatus, AcquiredImageStatusAdmin)