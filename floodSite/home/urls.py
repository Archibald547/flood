from django.conf.urls import url, include
from home import views
from home.regbackend import MyRegistrationView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from machina.app import board


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),name='registration_register'),
    url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'),name='registration_disallowed'),
    # url(r'^forum/', include(board.urls), name='forum'),
    url(r'^accounts/', include('registration.backends.simple.urls'), name="register"),
    url(r'^privacy_policy/$', views.privacy_policy.as_view(), name="privacy_policy"),

    url('^', include('django.contrib.auth.urls')),
    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('home:password_reset_done')),name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('home:password_reset_done')),name='password_reset'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('home:password_reset_comlete')),name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view,name='password_reset_complete'),
]
