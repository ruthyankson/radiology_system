from utils.helpers import to_list
from helpfuls.filters import room_choices, assigned_staff_choices, department_choices



# Form choices to list
# Room
# room_types_choices = to_list(room_type_choices())
# examinations_choices = to_list(examination_choices())
# machines_choices = to_list(machine_choices())

rooms_choices = to_list(room_choices())
staff_choices = to_list(assigned_staff_choices())
dept_choices = to_list(department_choices())
#
# job_des_choices = to_list(job_choices())
# educational_level_choices = to_list(edu_level_choices())