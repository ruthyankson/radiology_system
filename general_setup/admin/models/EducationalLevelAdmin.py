from django.contrib import admin

from general_setup.models.EducationalLevel import EducationalLevel
from general_setup.admin.forms.EducationalLevelFormAdmin import EducationalLevelFormAdmin

class EducationalLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    form = EducationalLevelFormAdmin
    search_fields = ['level']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(EducationalLevel, EducationalLevelAdmin)

