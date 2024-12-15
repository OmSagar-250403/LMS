"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.urls import path
from home.views import *

urlpatterns = [
    path('add-app', add_app, name='add_app'),
    path('get-app/', get_app, name='get_app'),  # Changed to match query parameter
    path('delete-app/<int:id>', delete_app, name='delete_app'),
    path('', app_management, name='app_management'),
]
