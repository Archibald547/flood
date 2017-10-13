from django.conf.urls import url, include
from home import views



urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^accounts/', include('registration.backends.default.urls'), name="register"),
    url(r'^privacy_policy/$', views.privacy_policy.as_view(), name="privacy_policy"),
]
