from django.contrib import admin
from patients.models.ImageRequest import ImageRequest


class ImageRequestAdmin(admin.ModelAdmin):
    list_display = ("patient", "request_date", "ward", "medical_officer",)
    search_fields = ["note_title"]
    fields = ["patient", "request_date", "ward", "brief_clinical_history",
                "radiological_investigation_requested", "medical_officer",
              "department", "radiology_serial_number", "previous_exams_details"
              ]

admin.site.register(ImageRequest, ImageRequestAdmin)