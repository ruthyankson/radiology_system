from django.contrib import admin
from patients.admin.forms.PatientFormAdmin import PatientFormAdmin
from django.urls import path, reverse
from django.utils.html import format_html
from django.contrib.auth.decorators import login_required

from patients.models.Patient import Patient
from patients.admin.views.PatientDetailView import PatientDetailView

# @admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
  actions = None
  list_display = ("hospital_number", "patient_type", "name", "gender", "detail")
  ordering = ("-created",)
  list_display_links = None
  fields = ["hospital_number", "patient_type", "name", 
          "date_of_birth", "age", "gender",
            "contact", "address",
            "pregnant" 
            ]
  # list_display_links = ["name"]
  search_fields = ["name"]
  form = PatientFormAdmin
  radio_fields = {"gender": admin.VERTICAL, "pregnant": admin.VERTICAL}
  # change_form_template = 'admin/site_change_form.html'


  def save_model(self, request, obj, form, change):
      obj.created_by = request.user
      obj.save()

  def get_urls(self):
    return [
            path(
                "<pk>",
                login_required(self.admin_site.admin_view(PatientDetailView.as_view())),
                name=f"patient_detail",
            ),
            *super().get_urls(),
        ]

  def detail(self, obj: Patient) -> str:
        url = reverse("admin:patient_detail", args=[obj.pk])
        return format_html(f'<a href="{url}"><i class="fas fa-eye ml-3"></i></a>')



admin.site.register(Patient, PatientAdmin)