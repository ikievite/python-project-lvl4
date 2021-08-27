from django.urls import path

from .views import UserDeleteView, UserListView, UserUpdateView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='create-user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update-user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete-user'),
]
