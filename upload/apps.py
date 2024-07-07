"""
This module defines the configuration for the 'upload' application.
"""

from django.apps import AppConfig


class UploadConfig(AppConfig):
    """
    Configuration for the 'upload' Django application.

    This class is used to configure settings for the 'upload' app,
    including specifying the default type for auto-generated
    primary keys and the name of the application.

    Attributes:
        default_auto_field (str): The default field type for
        auto-generated primary keys.
        name (str): The name of the Django application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload'
