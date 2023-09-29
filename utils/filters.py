# from django.contrib.auth import get_user_model
#
# from patients.models.Patient import Patient
# from patients.models.AcquiredImageStatus import AcquiredImageStatus
# from patients.models.ImagingRecord import ImagingRecord
# from patients.models.ImageRejectReasons import ImageRejectReasons
#
# from general_setup.models.RejectFactor import RejectFactor
# from general_setup.models.RejectSubFactor import RejectSubFactor
# from general_setup.models.ExaminationType import ExaminationType
# from general_setup.models.EducationalLevel import EducationalLevel
# from general_setup.models.Job import Job
#
# from facility.models.Room import Room
# from facility.models.ExaminationRoom import ExaminationRoom
# from facility.models.RoomType import RoomType
# from facility.models.Machine import Machine
#
# from datetime import date
#
# User = get_user_model()
#
# # Model object totals
# total_acquired_images = AcquiredImageStatus.objects.count()
# total_rooms = Room.objects.count()
#
# # Specific value totals
# total_reject = AcquiredImageStatus.objects.filter(image_status='Rejected').count()
# total_accept = AcquiredImageStatus.objects.filter(image_status='Accepted').count()
# total_non_repeated = ImagingRecord.objects.filter(examination_repeat_type='NRE').count()
# total_repeated = ImagingRecord.objects.filter(examination_repeat_type='RE').count()
# total_manual = ImagingRecord.objects.filter(setup_type='Manual').count()
# total_ace = ImagingRecord.objects.filter(setup_type='aec').count()
#
# # Multiselect totals
# total_examinations = ImagingRecord.examination_type.through.objects.count()
# total_factors = ImageRejectReasons.factors.through.objects.count()
#
# # Multi-selects
# selected_examination_types = ExaminationType.objects.all()
# selected_factors = RejectFactor.objects.all()
# selected_subfactors = RejectSubFactor.objects.all()
#
# # Value filters
# rejected_images = AcquiredImageStatus.objects.filter(image_status='Rejected')
# accepted_images = AcquiredImageStatus.objects.filter(image_status='Accepted')
#
# # Constants
# PERCENTAGE = 100
#
# # Record-based totals on field values
# def total_specific_exam(selected_exams):
#     selected_records_total = ImagingRecord.objects.filter(examination_type=selected_exams).count()
#     return selected_records_total
#
# def total_specific_factors(selected_factors):
#     selected_records_total = ImageRejectReasons.objects.filter(factors=selected_factors).count()
#     return selected_records_total
#
# def total_specific_sub_factors(selected_sub_factors):
#     selected_records_total = ImageRejectReasons.objects.filter(sub_factors=selected_sub_factors).count()
#     return selected_records_total
#
# # Filtering based on date range
# def date_based_imaging(start_d, end_d):
#     start_date = date(start_d)
#     end_date = date(end_d)
#     records_in_range = ImagingRecord.objects.filter(created__gte=start_date, created__lte=end_date)
#     return records_in_range
#
# def date_based_acquired_images(start_d, end_d):
#     start_date = date(start_d)
#     end_date = date(end_d)
#     records_in_range = AcquiredImageStatus.objects.filter(created__gte=start_date, created__lte=end_date)
#     return records_in_range
#
# # Any rate
# def any_rate(total_main, total_part):
#     total_main = float(total_main)
#     total_part = float(total_part)
#     if total_main != 0:
#         some_rate = (total_part / total_main) * PERCENTAGE
#     else:
#         some_rate = 0.0
#     return round(some_rate, 2)
#
#
# # Choices from models
# def edu_level_choices():
#     return [(item.level, item.level) for item in EducationalLevel.objects.all()]
#
# def job_choices():
#     return [(item.job_description, item.job_description) for item in Job.objects.all()]
#
# def assigned_staff_choices():
#     return [(item.name, item.name) for item in User.objects.all()]
#
# def room_choices():
#     return [(item.examination, item.examination) for item in Room.objects.all()]
#
# def examination_choices():
#     return [(item.examination, item.examination) for item in ExaminationRoom.objects.all()]
#
# def room_type_choices():
#     return [(item.type_of_room, item.type_of_room) for item in RoomType.objects.all()]
#
# def machine_choices():
#     return [(item.machine_name, item.machine_name) for item in Machine.objects.all()]
