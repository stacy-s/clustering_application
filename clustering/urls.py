from django.urls import path
from .views import *



urlpatterns = [
    path('clustering/', AlgorithmView.as_view(), name='clustering_url'),
    # path('clustering/import-file/', AlgorithmView.import_file, name='clustering_url'),
]