"""
This module registers the `UploadFile` model with the Django admin site.

By registering the `UploadFile` model, it becomes manageable through the
Django admin interface.

This registration allows for CRUD operations (Create, Read, Update, Delete)
on `UploadFile` instances via the Django admin panel.

Imports:
    - admin: Django's module for creating admin interfaces.
    - UploadFile: The model to be registered with the admin site.
    - timezone: The module for checking expired link.
"""

from django.contrib import admin
from .models import UploadFile
from django.utils import timezone

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_size', 'upload_date', 'upload_by', 'expiration_date', 'is_expired')
    search_fields = ('file_name', 'upload_by__username')
    list_filter = ('upload_date', 'expiration_date')
    readonly_fields = ('download_link', 'delete_link')

    def is_expired(self, obj):
        return obj.expiration_date and obj.expiration_date < timezone.now()
    is_expired.boolean = True 
    is_expired.short_description = 'Expired'

admin.site.register(UploadFile, UploadFileAdmin)
