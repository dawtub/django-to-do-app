from django.views import generic
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


class CreateTaskView(generic.CreateView):
    form_class = TaskForm
    template_name = 'tasks/new.html'
    success_url = reverse_lazy('tasks:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_list"] = Task.objects.all()
        return context


class TasksView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/index.html'
    success_url = reverse_lazy('tasks:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_list"] = self.model.objects.order_by('-time')
        return context


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
