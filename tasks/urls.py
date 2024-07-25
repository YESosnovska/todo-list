from django.urls import path

from tasks.views import TaskListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
]


app_name = "tasks"
