from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register/$',views.rego, name="register"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r'^profile', views.profile, name="profile"),
    url(r'', views.home, name="home"),
]
