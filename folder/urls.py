from django.urls import path
from .views import HomeView, TestView

app_name = 'folder'

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('test/', TestView.as_view(), name='test'), 
     
]