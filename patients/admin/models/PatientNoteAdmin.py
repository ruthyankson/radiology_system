from django.contrib import admin
from patients.models.PatientNote import PatientNote
from patients.admin.forms.PatientNoteFormAdmin import PatientNoteFormAdmin


class PatientNoteAdmin(admin.ModelAdmin):
    list_display = ("patient", "note_title", "note_date",)
    ordering = ("-created",)
    search_fields = ["patient", "note_title"]
    exclude = ["id", "status", "deactivate_date", "created_by", "note_date"]
    # readonly_fields = ["patient"]
    form = PatientNoteFormAdmin
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(PatientNote, PatientNoteAdmin)