from django.conf.urls import url, include
from dashboard import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard.as_view(), name="dashboard"),
    url(r'^profile/$', views.profile.as_view(), name="profile"),
]