from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import MyProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = MyProfile
        fields = ('user','exp','username')
