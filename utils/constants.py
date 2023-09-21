# constants.py

# App name
APP_NAME = "radiology-system"

# Status options for a model
STATUS_ACTIVE = 'active'
STATUS_INACTIVE = 'inactive'
STATUS_CHOICES = (
    (STATUS_ACTIVE, 'Active'),
    (STATUS_INACTIVE, 'Inactive'),
)

# User roles
ROLE_ADMIN = 'admin'
ROLE_USER = 'user'
ROLE_CHOICES = (
    (ROLE_ADMIN, 'Admin'),
    (ROLE_USER, 'User'),
)

# Staff roles / Groups
HOD = 'Head of Department'
COMMON_STAFF = 'Common Staff'

# Model Choices
ADMINISTRATION = 'AD'
RADIOLOGY = 'RD'
DEPARTMENTS = ["Administration", "Radiology"]

# Db_Seeder Values
JOBS = ['Biostatistics', 'Nurse', 'Radiologist', 
        'Radiographer', 'Medical Physicist', 
        'Biomedical Engineer', 'Radiation Protection Officer']

EDUCATIONAL_LEVELS = ["BSc. Degree", "MSc. Degree", "Ph.D Degree"]

EXAMINATION_TYPES = ["Abdomen", "Chest", "Knee", "Pelvis", "Cervical Spine", "Lumbar Spine", "Thoracic Spine"]

REJECT_FACTORS = ["Clear Image", "Damaged", "Unused Image", "Good but cannot be used for diagnosis"]

REJECT_SUB_FACTORS = ["Overexposure", "Underexposure", "Positioning error", "Equipment failure", "Patient motion"]


# Facility Values
ROOM_TYPES = ["Reading", "Imaging"]

EXAMINATIONS = ["CT", "Radiology", "Fluoroscopy", "Dental", "Mammography", "MRI"]

# Gender
MALE = 'M'
FEMALE = 'F'
GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

# Work Experience
LESS_SIX_MONTHS = '<6M'
SIX_MONTHS_ONE_HALF_YEAR = '6M-1.5Y'
ONE_HALF_FIVE_YEARS = '1.5Y-5Y'
MORE_THAN_FIVE_YEARS = '>5Y'

WORK_EXPERIENCE = [
    (LESS_SIX_MONTHS, "Less than 6 months"),
    (SIX_MONTHS_ONE_HALF_YEAR, "6 months - 1.5 years"),
    (ONE_HALF_FIVE_YEARS, "1.5 - 5 years",) ,
    (MORE_THAN_FIVE_YEARS, "More than 5 years")
]


# Patient types
INPATIENT = 'Inpatient'
OUTPATIENT = 'Outpatient'
PATIENT_TYPES = [(INPATIENT, "Inpatient"),
                 (OUTPATIENT, "Outpatient")
                 ]

# Yes/No choice
NA = 'N/A'
YES = 'Yes'
NO = 'No'
YES_NO = [(YES, 'Yes'),
          (NO, 'No')
          ]

# Imaging Record
NON_REPEATED_EXAMINATION = 'NRE'
REPEATED_EXAMINATION = 'RE'
EXAMINATION_REPEAT_TYPE = [
    (NON_REPEATED_EXAMINATION, "Non-Repeated Examination"),
    (REPEATED_EXAMINATION, "Repeated Examination")
]
AEC = 'AEC'
MANUAL_SETUP = 'Manual'
PATIENT_SETUP_TYPES = [
    (AEC, "AEC"),
    (MANUAL_SETUP, "Manual")
]

# General Statuses
PENDING = 'Pending'
COMPLETED = 'Completed'
DONE = 'Done'
UNDONE = 'Undone'
APPROVED = 'Approved'
REJECTED = 'Rejected'
ACCEPTED = 'Accepted'

# Acquired Image Status
ACQUIRED_IMAGE_STATUS = [
    (ACCEPTED, "Accepted"),
    (REJECTED, "Rejected")
]

# Maximum length for certain fields
MAX_TITLE_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 500

# Error messages
ERROR_INVALID_INPUT = "Invalid input. Please check your data."

# ... add more constants as needed ...

