"""
This module defines the URL patterns for the file-related views in the
application.

Each URL pattern is associated with a view function from the views module.
These patterns are used by Django to route HTTP requests to the appropriate
view based on the URL path.

URL patterns:
    - 'file/<str:file_token>': Routes to the file view, displaying a specific
    file based on the file token.
    - 'file/user/dl/<str:file_token>': Routes to the user_dl view, handling the
    download of a file by a user.
    - 'file/delete/<str:file_token>': Routes to the delete view, allowing the
    user to delete a specific file based on the file token.
    - 'file/error/': Routes to the file_error view, displaying an error page
    related to file operations.

Imports:
    - path: A function from django.urls for defining URL patterns.
    - views: The views module where the view functions are defined.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('file/<str:file_token>', views.file, name='file'),
    path('file/user/dl/<str:file_token>', views.user_dl, name='user_dl'),
    path('file/delete/<str:file_token>', views.delete, name='delete'),
    path('file/error/', views.file_error, name='file_error'),
]
