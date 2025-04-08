from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Folder

class HomeView(ListView):
    template_name = 'home.html'
    queryset = Folder.objects.all()
    context_object_name = 'folders'

class FolderDetailView(DetailView):
    model = Folder
    template_name = 'detail.html'
    context_object_name = 'folder'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
