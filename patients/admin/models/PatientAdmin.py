from django.contrib import admin
from patients.models.Patient import Patient
from patients.admin.forms.PatientFormAdmin import PatientFormAdmin


class PatientAdmin(admin.ModelAdmin):
    # def get_changeform_initial_data(self, request):
    #     get_data = super(PatientAdmin, self).get_changeform_initial_data(request)
    #     get_data['created_by'] = request.user.pk
    #     return get_data
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

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Patient, PatientAdmin)