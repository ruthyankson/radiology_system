from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from django.contrib.auth.decorators import login_required

from patients.models.ImagingRecord import ImagingRecord
from patients.admin.forms.ImagingRecordFormAdmin import ImagingRecordFormAdmin
from patients.admin.views.ImagingRecordDetailView import ImagingRecordDetailView


class ImagingRecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "examination_room", "record_date", "radiology_staff_id", "detail")
    ordering = ("-created",)
    # list_display_links = None
    search_fields = ["patient__name", "setup_type", "examination_type__type_name",
                     "examination_repeat_type", "radiology_staff_id", "examination_room__examination__examination"]
    list_per_page = 15
    fields = ["patient", "record_date", "radiology_staff_id",
              "examination_room", "examination_repeat_type",
              "examination_type", "setup_type",
              "ctdi",
              "radiation_quality", "radiation_quantity",
              "current", "radiation_time",
              "dose_area_product", "dose_length_product"
              ]
    readonly_fields = ["patient",]
    form = ImagingRecordFormAdmin

    def get_urls(self):
      return [
              path(
                  "<pk>",
                  login_required(self.admin_site.admin_view(ImagingRecordDetailView.as_view())),
                  name=f"imaging_record_detail",
              ),
              *super().get_urls(),
          ]

    def detail(self, obj: ImagingRecord) -> str:
          url = reverse("admin:imaging_record_detail", args=[obj.pk])
          return format_html(f'<a href="{url}"><i class="fas fa-eye ml-3"></i></a>')


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ImagingRecord, ImagingRecordAdmin)