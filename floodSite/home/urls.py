from django.conf.urls import url, include
from home import views
from machina.app import board


urlpatterns = [
    url(r'^$', views.home, name="home"),
    # url(r'^forum/', include(board.urls), name='forum'),
    url(r'^accounts/', include('registration.backends.simple.urls'), name="register"),
    url(r'^privacy_policy/$', views.privacy_policy.as_view(), name="privacy_policy"),
    # url(r'^about/$', views.about.as_view(), name="about"),
    # url(r'^contact/$', views.contact.as_view(), name="contact"),
]
