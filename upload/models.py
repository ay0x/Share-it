from django.db import models
from django.utils import timezone

class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=255)
    file_size = models.PositiveBigIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    upload_by = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        if not self.file_name:
            self.file_name = self.file.name
        if not self.file_size:
            self.file_size = self.file.size
        super().save(*args, **kwargs)
