# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class Profile(Models.model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     exp = models.IntegerField(default='0')
#     bio = models.TextField(max_length=500, blank=True, null=True)
#     location = models.CharField(max_length=30, blank=True, null=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
