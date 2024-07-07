"""
This module defines the configuration for the 'signup' application.

The SignupConfig class sets the default auto field type and
specifies the name of the application.
"""

from django.apps import AppConfig


class SignupConfig(AppConfig):
    """
    Configuration class for the 'signup' application.

    This class sets the default type of auto-incrementing
    primary key field to 'BigAutoField' and specifies
    the name of the application as 'signup'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signup'
