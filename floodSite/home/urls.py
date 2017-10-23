from django.conf.urls import url, include
from home import views
from home.regbackend import MyRegistrationView
from django.views.generic import TemplateView
from machina.app import board


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),name='registration_register'),
    url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'),name='registration_disallowed'),
    # url(r'^forum/', include(board.urls), name='forum'),
    url(r'^accounts/', include('registration.backends.simple.urls'), name="register"),
    url(r'^privacy_policy/$', views.privacy_policy.as_view(), name="privacy_policy"),
    # url(r'^about/$', views.about.as_view(), name="about"),
    # url(r'^contact/$', views.contact.as_view(), name="contact"),
]
