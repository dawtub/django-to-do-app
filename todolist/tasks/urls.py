from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TasksView.as_view(), name='index'),
    path('add/', views.CreateTaskView.as_view(), name='add')
]
