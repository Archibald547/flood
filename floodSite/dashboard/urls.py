from django.conf.urls import url, include
from dashboard import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^profile/$', views.profile.as_view(), name="profile"),
    url(r'^update_profile/$', views.update_profile, name="update_profile"),
    url(r'^reset_password/$', views.reset_password.as_view(), name="reset_password"),
]
