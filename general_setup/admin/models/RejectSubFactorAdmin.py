from django.contrib import admin
from general_setup.models.RejectSubFactor import RejectSubFactor
from general_setup.admin.forms.RejectSubFactorFormAdmin import RejectSubFactorFormAdmin


class RejectSubFactorAdmin(admin.ModelAdmin):
    list_display = ('sub_factor',)
    form = RejectSubFactorFormAdmin
    search_fields = ['sub_factor']

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(RejectSubFactor, RejectSubFactorAdmin)
