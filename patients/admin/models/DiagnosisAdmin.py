from django.contrib import admin
from patients.models.Diagnosis import Diagnosis
from patients.admin.forms.DiagnosisFormAdmin import DiagnosisFormAdmin


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("patient", "requesting_physician", "study_date",)
    search_fields = ["patient", "requesting_physician"]
    exclude = ["id", "status", "deactivate_date"]
    # form = DiagnosisFormAdmin

admin.site.register(Diagnosis, DiagnosisAdmin)