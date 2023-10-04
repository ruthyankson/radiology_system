from django.contrib import admin
from patients.models.Diagnosis import Diagnosis
from patients.admin.forms.DiagnosisFormAdmin import DiagnosisFormAdmin


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("patient", "requesting_physician", "study_date",)
    search_fields = ["patient__name", "requesting_physician"]
    readonly_fields = ["patient"]
    exclude = ["id", "status", "deactivate_date"]
    # form = DiagnosisFormAdmin

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Diagnosis, DiagnosisAdmin)