from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from django.contrib.auth.decorators import login_required

from patients.models.ImageRequest import ImageRequest
from patients.admin.views.ImageRequestDetailView import ImageRequestDetailView


class ImageRequestAdmin(admin.ModelAdmin):
    list_display = ("patient", "request_date", "ward", "medical_officer", "detail")
    ordering = ("-created",)
    list_display_links = None
    search_fields = ["note_title"]
    readonly_fields = ["patient"]
    fields = ["patient", "request_date", "ward", "brief_clinical_history",
                "radiological_investigation_requested", "medical_officer",
              "department", "radiology_serial_number", "previous_exams_details"
              ]

    def get_urls(self):
      return [
              path(
                  "<pk>",
                  login_required(self.admin_site.admin_view(ImageRequestDetailView.as_view())),
                  name=f"image_request_detail",
              ),
              *super().get_urls(),
          ]

    def detail(self, obj: ImageRequest) -> str:
          url = reverse("admin:image_request_detail", args=[obj.pk])
          return format_html(f'<a href="{url}"><i class="fas fa-eye ml-3"></i></a>')


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(ImageRequest, ImageRequestAdmin)