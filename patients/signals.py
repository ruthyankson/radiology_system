from django.db.models.signals import post_save
from patients.models.ImageRequest import ImageRequest
from django.dispatch import receiver
from patients.models.ImageRequestApproval import ImageRequestApproval
from patients.models.AcquiredImageStatus import AcquiredImageStatus
from django.contrib.auth import get_user_model


userHere = get_user_model()
image_request = ImageRequest

# @receiver(post_save, sender=image_request)
# def create_image_request_approval(sender, instance, created, **kwargs):
#     if created:
#         ImageRequestApproval.objects.create(image_request=instance)


# @receiver(post_save, sender=userHere)
# def create_acquired_image_status(sender, instance, created, **kwargs):
#     if created:
#         AcquiredImageStatus.objects.create(imaging_record=instance, created_by=instance)