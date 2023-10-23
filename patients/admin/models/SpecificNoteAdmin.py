from django.contrib import admin
from patients.models.SpecificNote import SpecificNote
from patients.admin.forms.SpecificNoteFormAdmin import SpecificNoteFormAdmin


class SpecificNoteAdmin(admin.ModelAdmin):
    list_display = ("patient", "weight", "type_of_procedure", "note_date",)
    ordering = ("-created",)
    ordering = ("-created",)
    search_fields = ["patient__name", "weight", "type_of_procedure"]
    exclude = ["id", "status", "deactivate_date", "created_by", "note_date"]
    # readonly_fields = ["patient"]
    form = SpecificNoteFormAdmin
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(SpecificNote, SpecificNoteAdmin)