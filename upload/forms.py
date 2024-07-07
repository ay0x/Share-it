"""
This module defines custom form fields and a form for handling file uploads.

It includes a custom file input widget that supports multiple file selection,
a file field that processes multiple files, and a form for uploading files.
"""
from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    """
    Custom file input widget that allows multiple file selection.

    Attributes:
        allow_multiple_selected (bool): Enables multiple file
        selection in the input.
    """
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """
    Custom file field that supports multiple file uploads.

    This field uses the MultipleFileInput widget and processes multiple files.

    Methods:
        __init__(*args, **kwargs): Initializes the field with
        the custom widget.
        clean(data, initial=None): Cleans the input data,
        handling multiple files.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        """
        Cleans the input data, processing multiple file uploads.

        Args:
            data (list, tuple, or None): The file data to clean.
            initial (None): Initial value for the field, unused here.

        Returns:
            list: A list of cleaned file data.
        """
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class UploadFileForm(forms.Form):
    """
    A form for handling file uploads.

    Uses the MultipleFileField to allow users to upload multiple files.

    Fields:
        files (MultipleFileField): A field for uploading multiple files.
    """
    files = MultipleFileField()
