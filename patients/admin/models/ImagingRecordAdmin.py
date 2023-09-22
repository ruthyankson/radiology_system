from django.contrib import admin
from patients.models.ImagingRecord import ImagingRecord
from patients.admin.forms.ImagingRecordFormAdmin import ImagingRecordFormAdmin


class ImagingRecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "examination_room", "record_date", "radiology_staff_id",)
    search_fields = ["patient", "examination_room"]
    fields = ["patient", "record_date", "radiology_staff_id",
              ("examination_room", "examination_repeat_type"),
              ("examination_type", "setup_type"),
              "ctdi",
              ("radiation_quality", "radiation_quantity"),
              ("current", "radiation_time"),
              ("dose_area_product", "dose_length_product")
              ]
    form = ImagingRecordFormAdmin

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ImagingRecord, ImagingRecordAdmin)