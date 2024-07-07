"""
This module defines URL patterns for the 'signup' application.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
