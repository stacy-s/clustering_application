from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('clustering/', AlgorithmView.as_view(), name='clustering_url'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]