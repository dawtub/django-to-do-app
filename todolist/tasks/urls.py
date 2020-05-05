from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TasksView.as_view(), name='index'),
    path('add/', views.TasksView.as_view(), name='add'),
    path('<int:pk>/delete', views.DeleteTask.as_view(), name='delete'),
    path('<int:task_id>/complete', views.complete, name='complete'),
]
