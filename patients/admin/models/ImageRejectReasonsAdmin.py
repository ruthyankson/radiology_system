from django.contrib import admin
from patients.models.ImageRejectReasons import ImageRejectReasons
from helpfuls.filters import rejected_images


class ImageRejectReasonsAdmin(admin.ModelAdmin):
    list_display = ("patient", "radiology_staff_id",)
    ordering = ("-created",)
    search_fields = ["patient__name", "radiology_staff_id", "factors__factor", "sub_factors__sub_factor"]
    readonly_fields = ["patient"]
    fields = ("radiology_staff_id", "factors", "sub_factors")

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(ImageRejectReasons, ImageRejectReasonsAdmin)