from django.urls import path
from . import views


urlpatterns = [
    path('', views.users, name='users'),
    path('create/', views.create, name='create-user'),
    path('<int:username_id>/update/', views.update, name='update-user'),
]
