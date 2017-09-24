from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/',views.rego, name="register"),
    url(r'', views.home, name="home"),
]
