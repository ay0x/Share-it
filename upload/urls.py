"""
This module defines URL patterns for the 'upload' application.

It maps URL paths to view functions for handling file uploads. The URL patterns
determine which view function should be called based on the requested URL.

Imports:
    - path: A function used to define URL patterns.
    - views: The module containing view functions to handle requests.

URL Patterns:
    - 'upload/': Maps to the `upload_file` view function, which handles
    file uploads.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
]
