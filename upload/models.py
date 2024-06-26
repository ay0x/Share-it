from django.db import models
from django.utils import timezone
from shareit.my_utils import generate_token
import uuid

class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=255)
    file_size = models.PositiveBigIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=24))
    upload_by = models.CharField(default='Guest', max_length=255)
    download_link = models.CharField(max_length=7, editable=False, unique=True)
    delete_link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        if not self.file_name:
            self.file_name = self.file.name
        if not self.file_size:
            self.file_size = self.file.size
        self.expiration_date = timezone.now() + timezone.timedelta(hours=24)
        self.download_link = generate_token()
        super().save(*args, **kwargs)
