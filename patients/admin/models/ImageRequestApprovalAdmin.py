from django.contrib import admin
from patients.models.ImageRequestApproval import ImageRequestApproval
from patients.admin.forms.ImageRequestApprovalFormAdmin import ImageRequestApprovalFormAdmin


class ImageRequestApprovalAdmin(admin.ModelAdmin):
    list_display = ("image_request", "approval")
    search_fields = ["image_request", "approval"]
    fields = ["image_request", "approval"]
    readonly_fields = ["image_request"]
    form = ImageRequestApprovalFormAdmin

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ImageRequestApproval, ImageRequestApprovalAdmin)