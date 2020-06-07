from django.urls import path
from .views import *



urlpatterns = [
    path('clustering/', import_file, name='clustering_url'),
    path('clustering/import-file/', import_file, name='clustering_url'),
]