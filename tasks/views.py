from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("tasks:index")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("tasks:index")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class ToggleTaskImplementation(generic.View):
    def post(self, request, pk, *args, **kwargs):
        task = Task.objects.get(id=pk)
        task.done = not task.done
        task.save()
        return HttpResponseRedirect(reverse_lazy("tasks:index"))
