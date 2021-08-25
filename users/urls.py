from django.urls import path

from . import views
from .views import UserDeleteView, UserListView, UserUpdateView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', views.create, name='create-user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update-user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete-user'),
]
