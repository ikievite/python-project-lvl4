from django.urls import path

from .views import StatusListView, StatusCreateView

urlpatterns = [
    path('', StatusListView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create-status'),
]
