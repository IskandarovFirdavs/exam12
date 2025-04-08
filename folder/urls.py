from django.urls import path
from .views import HomeView, FolderDetailView

app_name = 'folder'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('folder/<int:pk>/', FolderDetailView.as_view(), name='detail'),
]
