from django.contrib import admin
from facility.models.ExaminationRoom import ExaminationRoom
from facility.admin.forms.ExaminationRoomFormAdmin import ExaminationRoomFormAdmin


class ExaminationRoomAdmin(admin.ModelAdmin):
    list_display = ('examination',)
    form = ExaminationRoomFormAdmin
    search_fields = ['examination']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ExaminationRoom, ExaminationRoomAdmin)
