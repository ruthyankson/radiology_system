from django.urls import path
from patients.views.PatientChangeView import PatientChangeView

app_name = "patients"

urlpatterns = [
    # path('patient/add/', PatientChangeView.as_view(), name='new_patient'),
]
