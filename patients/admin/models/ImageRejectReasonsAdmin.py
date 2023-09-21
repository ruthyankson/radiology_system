from django.contrib import admin
from patients.models.ImageRejectReasons import ImageRejectReasons


class ImageRejectReasonsAdmin(admin.ModelAdmin):
    list_display = ("acquired_image_status", "radiology_staff_id",)
    search_fields = ["acquired_image_status", "radiology_staff_id",]
    fields = ("acquired_image_status", "radiology_staff_id", "factors", "sub_factors")

admin.site.register(ImageRejectReasons, ImageRejectReasonsAdmin)