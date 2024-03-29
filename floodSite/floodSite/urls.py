"""floodSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from machina.app import board
from rest_framework import routers
from api import views
from pusherchat import views as chatviews
from pusherchat2 import views as chatviews2
from pusherchat3 import views as chatviews3


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'myprofiles', views.MyProfileViewSet)
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^', include('dashboard.urls')),
    url(r'^forum/', include(board.urls)),
    # url(r'^schedule/', include('schedule.urls')),
    url(r'^', include('todoList.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^chat/', chatviews.chat),
    url(r'^ajax/chat/$', chatviews.broadcast),
    url(r'^chat2/', chatviews2.chat),
    url(r'^ajax/chat2/$', chatviews2.broadcast),
    url(r'^chat3/', chatviews3.chat),
    url(r'^ajax/chat3/$', chatviews3.broadcast),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# this static thing is only for development, not production

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document=settings.MEDIA_ROOT)
