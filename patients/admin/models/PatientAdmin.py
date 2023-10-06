from django.contrib import admin
from patients.admin.forms.PatientFormAdmin import PatientFormAdmin
from django.urls import path, reverse
from django.utils.html import format_html

from patients.models.Patient import Patient
from patients.admin.views.PatientDetailView import PatientDetailView

# @admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
  list_display = ("hospital_number", "patient_type", "name", "gender", "detail")
  fields = ["hospital_number", "patient_type", "name", 
          ("date_of_birth", "age"), "gender",
            ("contact", "address"),
            "pregnant" 
            ]
  list_display_links = ["name"]
  search_fields = ["name"]
  form = PatientFormAdmin
  # change_form_template = 'admin/site_change_form.html'


  def save_model(self, request, obj, form, change):
      obj.created_by = request.user
      obj.save()

  def get_urls(self):
    return [
            path(
                "patient/<pk>",
                self.admin_site.admin_view(PatientDetailView.as_view()),
                name=f"patient_detail",
            ),
            *super().get_urls(),
        ]

  def detail(self, obj: Patient) -> str:
        url = reverse("admin:patient_detail", args=[obj.pk])
        return format_html(f'<a href="{url}">👁</a>')



admin.site.register(Patient, PatientAdmin)