from django.conf.urls import url, include
from dashboard import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^profile/$', views.profile.as_view(), name="profile"),
    url(r'^update_profile/$', views.update_profile, name="update_profile"),
    url(r'^change_password/$', views.change_password, name="change_password"),
    url(r'^change_password/done/$', views.change_password_done, name="change_password_done"),
    url(r'^chatroom_list/$', views.chatroom_list.as_view(), name="chatroom_list"),
]
