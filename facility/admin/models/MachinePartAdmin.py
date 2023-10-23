from django.contrib import admin
from facility.models.MachinePart import MachinePart
from facility.admin.forms.MachinePartFormAdmin import MachinePartFormAdmin


class MachinePartAdmin(admin.ModelAdmin):
    list_display = ('machine', 'part', 'serial_number', 'model_number', 'date_of_manufacture')
    search_fields = ['part']
    fields = ['machine', 'part', 'serial_number', 'model_number', 'date_of_manufacture']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(MachinePart, MachinePartAdmin)
