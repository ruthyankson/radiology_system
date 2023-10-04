from django.contrib import admin
from patients.models.Patient import Patient
from patients.admin.forms.PatientFormAdmin import PatientFormAdmin

# @admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("hospital_number", "patient_type", "name",
                  "age", "gender",)
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



admin.site.register(Patient, PatientAdmin)