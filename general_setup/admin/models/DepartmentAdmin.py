from django.contrib import admin

from general_setup.models.Department import Department
from general_setup.admin.forms.DepartmentFormAdmin import DepartmentFormAdmin

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    form = DepartmentFormAdmin
    search_fields = ['department_name']
    view_on_site = False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Department, DepartmentAdmin)

