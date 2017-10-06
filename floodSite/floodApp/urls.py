from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^register/$',views.rego, name="register"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'home/$', views.home, name="home"),
    url(r'^login/$', login, {'template_name':'home/template/base.html'}, name="login"),
    url(r'^logout/$',logout, {'next_page':reverse_lazy('home')}, name="logout")
]
