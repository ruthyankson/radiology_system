from django.contrib import admin
from patients.models.ImageRejectReasons import ImageRejectReasons
from patients.models.AcquiredImageStatus import AcquiredImageStatus
from helpfuls.filters import rejected_images


class ImageRejectReasonsAdmin(admin.ModelAdmin):
    list_display = ("acquired_image_status", "radiology_staff_id",)
    search_fields = ["acquired_image_status", "radiology_staff_id", "factors__factor", "sub_factors__sub_factor"]
    readonly_fields = ["acquired_image_status"]
    fields = ("acquired_image_status", "radiology_staff_id", "factors", "sub_factors")

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['acquired_image_status'].queryset = rejected_images
        return super(ImageRejectReasonsAdmin, self).render_change_form(request, context, *args, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(ImageRejectReasons, ImageRejectReasonsAdmin)