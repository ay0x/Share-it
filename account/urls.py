"""
This module defines the URL patterns for the application.

Each URL pattern is associated with a view function from
the views module.

These patterns are used by Django to route HTTP requests
to the appropriate view based on the URL path.

URL patterns:
    - 'dashboard/': Routes to the dashboard view, displaying
    the main dashboard page.
    - 'profile/': Routes to the profile view, allowing users
    to view and update their profile information.
    - 'history/': Routes to the history view, displaying the
    user's file upload history with statuses.
    - 'logout/': Routes to the logout view, logging out the
    user and redirecting to the file upload page.

Imports:
    - path: A function from django.urls for defining URL patterns.
    - views: The views module where the view functions are defined.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('history/', views.history, name='history'),
    path('logout/', views.logout, name='logout'),
]
