from django.urls import path
from . import views


urlpatterns = [
    path('', views.users, name='users'),
    path('create', views.create, name='create-user'),
    path('update', views.update, name='update-user'),
]
