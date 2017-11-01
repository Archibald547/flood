from django.conf.urls import url, include
from todoList import views

urlpatterns = [
    url(r'^todo/$', views.index, name="todo"),
    url(r'^todo/list$', views.index, name="todo_view"),
    url(r'^todo/delete/(?P<pk>\d+)/$', views.delete_task, name="delete_task"),
    url(r'^todo/task/$', views.post_task, name="post_task"),
    url(r'^todo/task/edit/(?P<pk>\d+)/$', views.edit_task, name="edit_task"),
    url(r'^todo/complete/(?P<pk>\d+)/$', views.completed, name="completed"),
]
