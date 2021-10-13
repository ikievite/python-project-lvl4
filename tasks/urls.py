from django.urls import path

from . import views
from .views import TaskCreateView, TaskListView

urlpatterns = [
    path('', views.index, name='tasks-home'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/create/', TaskCreateView.as_view(), name='create-task'),
]
