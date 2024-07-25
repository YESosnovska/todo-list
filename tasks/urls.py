from django.urls import path

from tasks.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]


name = "todo_list"
