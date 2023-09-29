from django.contrib import admin

from general_setup.models.ExaminationType import ExaminationType
from general_setup.admin.forms.ExaminationTypeFormAdmin import ExaminationTypeFormAdmin

class ExaminationTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    form = ExaminationTypeFormAdmin
    search_fields = ['type_name']

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ExaminationType, ExaminationTypeAdmin)

