from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home.as_view(), name="home"),
    url(r'^privacy_policy/$', views.privacy_policy.as_view(), name="privacy_policy"),
]