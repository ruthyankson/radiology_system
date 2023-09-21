from django.contrib import admin
from facility.models.Machine import Machine
from facility.admin.forms.MachineFormAdmin import MachineFormAdmin


class MachineAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'description','image_tag', 'machine_image')
    form = MachineFormAdmin
    search_fields = ['machine_name']
    # fields = ['machine_name', 'description','image_tag', 'machine_image']


admin.site.register(Machine, MachineAdmin)
