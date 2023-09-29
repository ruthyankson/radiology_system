from django.contrib import admin
from accounts.models.Profile import Profile
from accounts.admin.forms.ProfileFormAdmin import ProfileFormAdmin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('designated_staff_id', 'user', 'job_description', 'contact')
    form = ProfileFormAdmin
    list_display_links = ('designated_staff_id', 'user')
    search_fields = ['user__name','designated_staff_id', 'job_description', 'gender']
    fields = ('user', 'designated_staff_id', 'title', 'job_description', 'gender', 'address', 'contact',
              'alternative_contact', 'date_of_birth', 'educational_level', 'work_experience', 'qualifications')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(Profile, ProfileAdmin)
