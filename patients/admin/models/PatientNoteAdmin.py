from django.contrib import admin
from patients.models.PatientNote import PatientNote


class PatientNoteAdmin(admin.ModelAdmin):
    list_display = ("patient", "note_title", "note_date",)
    search_fields = ["patient", "note_title"]
    exclude = ["id", "status", "deactivate_date"]

admin.site.register(PatientNote, PatientNoteAdmin)