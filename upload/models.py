"""
This module defines models for handling file uploads, including files that are
uploaded, deleted, and expired.
"""
from django.db import models
from django.utils import timezone
from shareit.my_utils import generate_token
import uuid
from django.conf import settings


class UploadFile(models.Model):
    """
    Model representing a file uploaded by a user.

    Attributes:
        file (FileField): The uploaded file.
        file_name (CharField): The name of the file.
        file_size (PositiveBigIntegerField): The size of the file
        in bytes.
        upload_date (DateTimeField): The date and time when the
        file was uploaded.
        expiration_date (DateTimeField): The date and time when
        the file will expire.
        upload_by (ForeignKey): The user who uploaded the file,
        or null if uploaded by a guest.
        download_link (CharField): A unique link for downloading the file.
        delete_link (UUIDField): A unique identifier for deleting the file.
    """

    file = models.FileField(upload_to='')
    file_name = models.CharField(max_length=255)
    file_size = models.PositiveBigIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=timezone.now()
                                           + timezone.timedelta(minutes=3))
    upload_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True,
                                  on_delete=models.DO_NOTHING)
    download_link = models.CharField(max_length=7,
                                     editable=False, unique=True)
    delete_link = models.UUIDField(default=uuid.uuid4,
                                   editable=False, unique=True)

    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        """
        Override the save method to populate file_name, file_size,
        and download_link before saving.

        If file_name or file_size is not provided, they are set to the
        file's name and size respectively.
        The expiration_date is set to 24 hours from the current time.
        A unique download_link is generated.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        if not self.file_name:
            self.file_name = self.file.name
        if not self.file_size:
            self.file_size = self.file.size
        if self.upload_by is None:
            self.upload_by = None
        self.expiration_date = timezone.now() + timezone.timedelta(minutes=3)
        self.download_link = generate_token()
        super().save(*args, **kwargs)


class DeletedFile(models.Model):
    """
    Model representing a file that has been deleted.

    Attributes:
        file_name (CharField): The name of the file.
        file_size (PositiveBigIntegerField): The size of the file in bytes.
        download_link (CharField): A unique link for downloading
        the file.
        upload_date (DateTimeField): The date and time when the
        file was uploaded.
        deletion_date (DateTimeField): The date and time when
        the file was deleted.
        upload_by (ForeignKey): The user who uploaded the file,
        or null if uploaded by a guest.
    """

    file_name = models.CharField(max_length=255)
    file_size = models.PositiveBigIntegerField()
    download_link = models.CharField(max_length=7, editable=False,
                                     default='V0Y4g3!')
    upload_date = models.DateTimeField()
    deletion_date = models.DateTimeField(default=timezone.now)
    upload_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.DO_NOTHING,
                                  null=True, blank=True)


class ExpiredFile(models.Model):
    """
    Model representing a file that has expired.

    Attributes:
        file_name (CharField): The name of the file.
        file_size (PositiveBigIntegerField): The size of the file in bytes.
        download_link (CharField): A unique link for downloading the file.
        upload_date (DateTimeField): The date and time when the
        file was uploaded.
        expiration_date (DateTimeField): The date and time when
        the file expired.
        expired_on (DateTimeField): The date and time when the
        file was marked as expired.
        upload_by (ForeignKey): The user who uploaded the file,
        or null if uploaded by a guest.
    """

    file_name = models.CharField(max_length=255)
    file_size = models.PositiveBigIntegerField()
    download_link = models.CharField(max_length=7, editable=False,
                                     default='voYage!')
    upload_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    expired_on = models.DateTimeField(default=timezone.now)
    upload_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.DO_NOTHING,
                                  null=True, blank=True)
