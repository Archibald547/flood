from django.conf.urls import url, include
from myTodo import views

urlpatterns = [
    url(r'^todo/$', views.index, name="todo"),
    url(r'^todo/task/$', views.post_task, name="post_task"),
    url(r'^todo/task/(?P<pk>\d+)/edit$', views.edit_task, name="edit_task"),
    # url(r'^todo/post/(?P<pk>\d+)/$', views.task_detail, name="task_detail"),
]
