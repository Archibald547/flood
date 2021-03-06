from django.contrib.auth.models import User
from .models import MyProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyProfile.objects.create(user=instance)
    instance.myprofile.save()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    created = MyProfile.objects.get_or_create(user= request.user)
    if created:
       profile = MyProfile(user=user)
    profile.save()
