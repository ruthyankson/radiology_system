from django.contrib import admin
from facility.models.MachinePart import MachinePart
from facility.admin.forms.MachinePartFormAdmin import MachinePartFormAdmin


class MachinePartAdmin(admin.ModelAdmin):
    list_display = ('machine', 'part', 'serial_number', 'model_number', 'date_of_manufacture')
    search_fields = ['part']
    fields = [('machine', 'part'), ('serial_number', 'model_number'), 'date_of_manufacture']


admin.site.register(MachinePart, MachinePartAdmin)
