from django.contrib import admin
from task_assignment.models.Task import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("deadline", "title", "assigned_staff", "status")
    list_display_links = ('deadline', 'title', 'assigned_staff')
    search_fields = ["deadline", "title", "image_status"]
    fields = ("deadline", "title", "task", "assigned_staff", "room", "department", "status")

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Task, TaskAdmin)