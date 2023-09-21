from django.contrib import admin

from general_setup.models.Holiday import Holiday
from general_setup.admin.forms.HolidayFormAdmin import HolidayFormAdmin

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('day_name', 'day_date',)
    fields = [('day_name', 'day_date'),]
    search_fields = ['day_name']


admin.site.register(Holiday, HolidayAdmin)

