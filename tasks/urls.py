from django.urls import path

from . import views
from .views import TaskListView

urlpatterns = [
    path('', views.index, name='tasks-home'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
]
