from django.contrib import admin
from patients.models.PostPreparationNote import PostPreparationNote
from patients.admin.forms.PostPreparationNoteFormAdmin import PostPreparationNoteFormAdmin


class PostPreparationNoteAdmin(admin.ModelAdmin):
    list_display = ("patient", "preparation_confirmation", "staff_signature", "preparation_date",)
    ordering = ("-created",)
    search_fields = ["patient__name", "preparation_confirmation", "staff_signature"]
    fields = ["preparation_confirmation", "injection_swelling", "staff_signature", "preparation_date",]
    # form = PostPreparationNoteFormAdmin

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(PostPreparationNote, PostPreparationNoteAdmin)