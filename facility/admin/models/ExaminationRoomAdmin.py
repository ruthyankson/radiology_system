from django.contrib import admin
from facility.models.ExaminationRoom import ExaminationRoom
from facility.admin.forms.ExaminationRoomFormAdmin import ExaminationRoomFormAdmin


class ExaminationRoomAdmin(admin.ModelAdmin):
    list_display = ('examination',)
    form = ExaminationRoomFormAdmin
    search_fields = ['examination']


admin.site.register(ExaminationRoom, ExaminationRoomAdmin)
