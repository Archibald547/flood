from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer,ProfileSerializer,TodoSerializer
from home.models import MyProfile
from todoList.models import todo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MyProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profiles to be viewed or edited.
    """
    queryset = MyProfile.objects.all()
    serializer_class = ProfileSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user todo tasks to be viewed or edited.
    """
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
