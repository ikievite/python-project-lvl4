from django.urls import path

from .views import StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView

urlpatterns = [
    path('', StatusListView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create-status'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='update-status'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete-status'),
]
