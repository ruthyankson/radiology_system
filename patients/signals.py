from django.db.models.signals import post_save
from patients.models.ImageRequest import ImageRequest
from django.dispatch import receiver
from patients.models.ImageRequestApproval import ImageRequestApproval

image_request = ImageRequest

@receiver(post_save, sender=image_request)
def create_image_request_approval(sender, instance, created, **kwargs):
    print("Sender --> ", sender)
    print("Instance -->", instance)
    print("Created --> ", created)
    if created:
        ImageRequestApproval.objects.create(image_request=instance)