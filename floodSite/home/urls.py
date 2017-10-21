from django.conf.urls import url, include
from home import views
from home.regbackend import MyRegistrationView



urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls'), name="register"),
    url(r'^privacy_policy/$', views.privacy_policy.as_view(), name="privacy_policy"),
]
