from django.contrib import admin
from facility.models.Room import Room
from facility.admin.forms.RoomFormAdmin import RoomFormAdmin


class RoomAdmin(admin.ModelAdmin):
    list_display = ('examination', 'room_type', 'description', 'machine')
    search_fields = ['room_type', 'examination', 'machine']
    fields = [("examination", "room_type"), "description", "machine"]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(Room, RoomAdmin)
