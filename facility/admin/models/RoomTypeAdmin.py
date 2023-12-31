from django.contrib import admin
from facility.models.RoomType import RoomType
from facility.admin.forms.RoomTypeFormAdmin import RoomTypeFormAdmin


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('type_of_room',)
    form = RoomTypeFormAdmin
    search_fields = ['type_of_room']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(RoomType, RoomTypeAdmin)
