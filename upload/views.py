"""
This module defines the view for uploading files in the 'file' application.
"""

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import UploadFile
from signup.models import User
from django.contrib import messages


def upload_file(request):
    """
    Handles file upload and returns a JSON response with file details.

    For POST requests, this view processes the uploaded files. It checks
    if the user is authenticated and enforces a file size limit for
    unauthenticated users.

    For each file uploaded, it creates an `UploadFile` instance, saves it,
    and returns a JSON response with details about the uploaded files.

    For GET requests, it renders the file upload form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A JSON response containing file details or a
        redirect to the upload page.
    """
    MAX_SIZE_UNAUTHENTICATED = 300 * 1024 * 1024  # Guest user 300MB limit
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_unique_gen_id = request.POST.get('uploader')
            try:
                user = User.objects.get(user_unique_gen_id=user_unique_gen_id)
            except User.DoesNotExist:
                user = None

            files = request.FILES.getlist('files')

            token_list = []
            file_list = []
            for file in files:
                if not user and file.size > MAX_SIZE_UNAUTHENTICATED:
                    messages.error(request, f"File {file.name} exceeds\
                        the 300MB limit for unauthenticated users.")
                    return redirect('upload_file')
                uploaded_file = UploadFile(file=file,
                                           upload_by=user if user else None)
                uploaded_file.save()
                token_list.append(uploaded_file.download_link)
                file_list.append({
                    'file_name': uploaded_file.file_name,
                    'file_size': uploaded_file.file_size,
                    'download_link': uploaded_file.download_link,
                    'delete_link': uploaded_file.delete_link
                })
            return JsonResponse({
                'show_download_list': True,
                'files': file_list
            })
    else:
        return render(request, 'pages/home.html')
