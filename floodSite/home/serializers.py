from rest_framework import serializers
from .models import MyProfile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyProfile
        fields = {'username', 'exp',}

