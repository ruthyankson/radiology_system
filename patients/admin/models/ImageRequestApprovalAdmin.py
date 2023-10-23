from django.contrib import admin
from patients.models.ImageRequestApproval import ImageRequestApproval
from patients.admin.forms.ImageRequestApprovalFormAdmin import ImageRequestApprovalFormAdmin


class ImageRequestApprovalAdmin(admin.ModelAdmin):
    # actions = None
    list_display = ("patient", "approval")
    ordering = ("-created",)
    # list_display_links = None
    search_fields = ["patient__name", "approval",]
    fields = ["patient", "approval",]
    readonly_fields = ["patient",]
    empty_value_display = "None"
    form = ImageRequestApprovalFormAdmin

    # def __init__(self, *args, **kwargs):
    #     super(ImageRequestApprovalAdmin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None, )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ImageRequestApproval, ImageRequestApprovalAdmin)