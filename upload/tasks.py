"""
This module defines a Celery task for checking the expiry of uploaded files.

It identifies files that have expired based on their expiration date,
moves them to the ExpiredFile model, and deletes them from the UploadFile
model.
"""
from celery import shared_task
from django.utils import timezone
from .models import UploadFile, ExpiredFile


@shared_task
def check_expiry():
    """
    A Celery task that checks for expired uploaded files, moves them to the
    ExpiredFile model, and deletes them from the UploadFile model.

    The task identifies files in the UploadFile model with an expiration date
    earlier than the current time, creates a corresponding entry in the
    ExpiredFile model, and then deletes the original file from the UploadFile
    model.

    This helps in managing the lifecycle of uploaded files and ensures that
    expired files are moved to a separate model for record-keeping.

    Returns:
        None
    """
    now = timezone.now()
    expired_files = UploadFile.objects.filter(expiration_date__lt=now)

    for file in expired_files:
        ExpiredFile.objects.create(
            file_name=file.file_name,
            file_size=file.file_size,
            download_link=file.download_link,
            upload_date=file.upload_date,
            expiration_date=file.expiration_date,
            upload_by=file.upload_by
        )
        file.delete()
