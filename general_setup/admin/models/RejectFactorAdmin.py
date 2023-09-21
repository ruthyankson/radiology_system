from django.contrib import admin
from general_setup.models.RejectFactor import RejectFactor
from general_setup.admin.forms.RejectFactorFormAdmin import RejectFactorFormAdmin


class RejectFactorAdmin(admin.ModelAdmin):
    list_display = ('factor',)
    form = RejectFactorFormAdmin
    search_fields = ['factor']

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(RejectFactor, RejectFactorAdmin)
