"""
This module defines the configuration for the 'file' app.

It includes the following configuration class:
    - FileConfig: Configures settings specific to the 'file' app.

Imports:
    - AppConfig: The base class for configuring apps in Django.
"""

from django.apps import AppConfig


class FileConfig(AppConfig):
    """
    Configuration class for the 'file' app.

    This class sets the default auto field type and the name of the app.

    Attributes:
        default_auto_field (str): The default type for auto-generated
        primary keys.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file'
