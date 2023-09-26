from patients.models.Patient import Patient
from patients.models.AcquiredImageStatus import AcquiredImageStatus
from patients.models.ImagingRecord import ImagingRecord
from patients.models.ImageRejectReasons import ImageRejectReasons

from general_setup.models.RejectFactor import RejectFactor
from general_setup.models.RejectSubFactor import RejectSubFactor
from general_setup.models.ExaminationType import ExaminationType

from facility.models.Room import Room

from datetime import date

# Model object totals
total_acquired_images = AcquiredImageStatus.objects.count()
total_rooms = Room.objects.count()

# Specific value totals
total_reject = AcquiredImageStatus.objects.filter(image_status='Rejected').count()
total_accept = AcquiredImageStatus.objects.filter(image_status='Accepted').count()
total_non_repeated = ImagingRecord.objects.filter(examination_repeat_type='NRE').count()
total_repeated = ImagingRecord.objects.filter(examination_repeat_type='RE').count()
total_manual = ImagingRecord.objects.filter(setup_type='Manual').count()
total_ace = ImagingRecord.objects.filter(setup_type='aec').count()

# Multiselect totals
total_examinations = ImagingRecord.examination_type.through.objects.count()
total_factors = ImageRejectReasons.factors.through.objects.count()

# Multi-selects
selected_examination_types = ExaminationType.objects.all()
selected_factors = RejectFactor.objects.all()
selected_subfactors = RejectSubFactor.objects.all()

# Value filters
rejected_images = AcquiredImageStatus.objects.filter(image_status='Rejected')
accepted_images = AcquiredImageStatus.objects.filter(image_status='Accepted')

# Constants
PERCENTAGE = 100

# Record-based totals on field values
def total_specific_exam(selected_exams):
    selected_records_total = ImagingRecord.objects.filter(examination_type=selected_exams).count()
    return selected_records_total

def total_specific_factors(selected_factors):
    selected_records_total = ImageRejectReasons.objects.filter(factors=selected_factors).count()
    return selected_records_total

def total_specific_sub_factors(selected_sub_factors):
    selected_records_total = ImageRejectReasons.objects.filter(sub_factors=selected_sub_factors).count()
    return selected_records_total

# Filtering based on date range
def date_based_imaging(start_d, end_d):
    start_date = date(start_d)
    end_date = date(end_d)
    records_in_range = ImagingRecord.objects.filter(created__gte=start_date, created__lte=end_date)
    return records_in_range

def date_based_acquired_images(start_d, end_d):
    start_date = date(start_d)
    end_date = date(end_d)
    records_in_range = AcquiredImageStatus.objects.filter(created__gte=start_date, created__lte=end_date)
    return records_in_range

# Any rate
def any_rate(total_main, total_part):
    total_main = float(total_main)
    total_part = float(total_part)
    if total_main != 0:
        some_rate = (total_part / total_main) * PERCENTAGE
    else:
        some_rate = 0.0
    return round(some_rate, 2)


# Use filter() to retrieve records within the date range