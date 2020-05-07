from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskForm


class TasksView(LoginRequiredMixin, generic.CreateView):
    model = Task
    login_url = reverse_lazy('users:login')
    form_class = TaskForm
    template_name = 'tasks/index.html'
    success_url = reverse_lazy('tasks:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {'user': self.request.user}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_list"] = self.model.objects\
            .filter(user=self.request.user)\
            .order_by('-time')
        return context


class DeleteTask(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def complete(self, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy('tasks:index'))

