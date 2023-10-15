from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from accounts.models.Profile import Profile

userHere = get_user_model()

@receiver(post_save, sender=userHere)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)