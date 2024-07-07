"""
This module registers the `UploadFile` model with the Django admin site.

By registering the `UploadFile` model, it becomes manageable through the
Django admin interface.

This registration allows for CRUD operations (Create, Read, Update, Delete)
on `UploadFile` instances via the Django admin panel.

Imports:
    - admin: Django's module for creating admin interfaces.
    - UploadFile: The model to be registered with the admin site.
"""

from django.contrib import admin
from .models import UploadFile


admin.site.register(UploadFile)
