from django.urls import path
from .views import UserDeleteView, UserUpdateView
from . import views


urlpatterns = [
    path('', views.users, name='users'),
    path('create/', views.create, name='create-user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update-user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete-user'),
]
