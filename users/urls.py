from django.urls import path
from .views import UserDeleteView
from . import views


urlpatterns = [
    path('', views.users, name='users'),
    path('create/', views.create, name='create-user'),
    path('<int:username_id>/update/', views.update, name='update-user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete-user'),
]
