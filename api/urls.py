from django.contrib import admin
from django.urls import path, include
from .views import CreateView

urlpatterns = [
    path('dataset/', CreateView.as_view(), name='create'),
]