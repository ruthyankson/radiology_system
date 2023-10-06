from django.urls import path
from patients.views.PatientDetailView import PatientDetailView

app_name = "patients"

urlpatterns = [
    path('patient-details/', PatientDetailView.as_view(), name='patient_details'),
]
