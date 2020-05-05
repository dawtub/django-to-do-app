from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


class TasksView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/index.html'
    success_url = reverse_lazy('tasks:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_list"] = self.model.objects.order_by('-time')
        return context


class DeleteTask(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def complete(self, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy('tasks:index'))

