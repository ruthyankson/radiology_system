from django.contrib import admin
from facility.models.Room import Room
from facility.admin.forms.RoomFormAdmin import RoomFormAdmin


class RoomAdmin(admin.ModelAdmin):
    list_display = ('examination', 'room_type', 'description', 'machine')
    search_fields = ['room_type']
    fields = [("examination", "room_type"), "description", "machine",]


admin.site.register(Room, RoomAdmin)
