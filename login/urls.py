"""
This module defines the URL patterns for the 'login' app.

Each URL pattern is associated with a view function from the views module.
These patterns are used by Django to route HTTP requests to the
appropriate view based on the URL path.

URL patterns:
    - 'login/': Routes to the user_login view, which handles user
    authentication.

Imports:
    - path: A function from django.urls for defining URL patterns.
    - views: The views module where the view functions are defined.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login')
]
