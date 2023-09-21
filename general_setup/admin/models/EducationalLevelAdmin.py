from django.contrib import admin

from general_setup.models.EducationalLevel import EducationalLevel
from general_setup.admin.forms.EducationalLevelFormAdmin import EducationalLevelFormAdmin

class EducationalLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    form = EducationalLevelFormAdmin
    search_fields = ['level']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(EducationalLevel, EducationalLevelAdmin)

