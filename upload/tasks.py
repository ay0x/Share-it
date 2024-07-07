# myapp/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import UploadFile, ExpiredFile

@shared_task
def check_expiry():
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
