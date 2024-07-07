"""
This module contains view functions for handling file-related operations.
"""

from django.shortcuts import render, redirect
from upload.models import UploadFile, DeletedFile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def file(request, file_token):
    """
    Displays a file for download based on its token.

    Args:
        request (HttpRequest): The HTTP request object.
        file_token (str): The unique token associated with the file.

    Returns:
        HttpResponse: The rendered template with file details if found,
                      otherwise redirects to the file error page.
    """
    try:
        file = UploadFile.objects.get(download_link=file_token)
        context = {
            'file_name': file.file_name,
            'file_size': file.file_size,
            'download_link': file.file.url
        }
        return render(request, 'file/download.html', context)
    except UploadFile.DoesNotExist:
        return redirect('file_error')


@login_required(login_url='/login/')
def user_dl(request, file_token):
    """
    Handles user-specific download functionality and restricts
    access if the user is not the uploader.

    Args:
        request (HttpRequest): The HTTP request object.
        file_token (str): The unique token associated with the file.

    Returns:
        HttpResponse: The rendered template with file details if the
        user is the uploader, or an error message and a restricted
        file view if the user is not the uploader.
        Redirects to the file error page if the file is not found.
    """
    try:
        file = UploadFile.objects.get(download_link=file_token)

        # Check if the logged-in user is the uploader
        if file.upload_by != request.user:
            context = {
                'file_name': file.file_name,
                'file_size': file.file_size,
                'download_link': file.file.url
            }
            messages.error(request, 'You cannot access this part\
                           of the file because you are not the uploader.')
            return render(request, 'file/download.html', context)
        else:
            context = {
                'file_name': file.file_name,
                'file_size': file.file_size,
                'download_link': file.download_link,
                'delete_link': file.delete_link
            }
            return render(request, 'file/user_download.html', context)
    except UploadFile.DoesNotExist:
        return redirect('file_error')


def delete(request, file_token):
    """
    Allows the user to delete a file and move it to
    the DeletedFile model.

    Handles both GET and POST requests. For GET requests,
    it displays a confirmation page. For POST requests, it deletes
    the file and creates a record in the DeletedFile model.

    Args:
        request (HttpRequest): The HTTP request object.
        file_token (str): The unique token associated with the file.

    Returns:
        HttpResponse: A redirect to the upload file page upon
        successful deletion, or the rendered delete confirmation
        page if the request is GET.
        Redirects to the file error page if the file is not found.
    """
    try:
        file = UploadFile.objects.get(delete_link=file_token)

        if request.method == 'POST':
            # Save file information to DeletedFile model
            DeletedFile.objects.create(
                file_name=file.file_name,
                file_size=file.file_size,
                download_link=file.download_link,
                upload_date=file.upload_date,
                upload_by=file.upload_by
            )
            file.delete()
            messages.success(request, 'File deleted successfully.')
            return redirect('upload_file')

        context = {
            'file_name': file.file_name,
            'file_size': file.file_size,
            'delete_link': file.delete_link
        }
        return render(request, 'file/delete.html', context)

    except UploadFile.DoesNotExist:
        return redirect('file_error')


def file_error(request):
    """
    Displays an error page for file-related issues.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered error page for file-related issues.
    """
    return render(request, 'file/download_error.html')
