from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models import Profile
# from django.forms import Textarea

class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    exp = models.IntegerField(default='0')
    country = CountryField(blank_label='(select country)')
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500)

#from django.contrib.auth.models import User
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         MyProfile.objects.create(user=instance)
#     instance.myprofile.save()
#
# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     created = MyProfile.objects.get_or_create(user= request.user)
#     if created:
#        profile = MyProfile(user=user)
#     profile.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
