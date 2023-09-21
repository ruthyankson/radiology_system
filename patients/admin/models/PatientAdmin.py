from django.contrib import admin
from patients.models.Patient import Patient
from patients.admin.forms.PatientFormAdmin import PatientFormAdmin


class PatientAdmin(admin.ModelAdmin):
    list_display = ("hospital_number", "patient_type", "name",
                  "age", "gender",)
    fields = [("hospital_number", "patient_type"),
              ("name", "date_of_birth"),
              ("age", "gender"),
              ("pregnant", "contact"),
              "address",
              ]
    list_display_links = ["name"]
    search_fields = ["name"]
    form = PatientFormAdmin

admin.site.register(Patient, PatientAdmin)