from django.shortcuts import render, redirect
from upload.models import UploadFile, DeletedFile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def file(request, file_token):
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
    try:
        file = UploadFile.objects.get(download_link=file_token)
        
        # Check if the logged-in user is the uploader
        if file.upload_by != request.user:
            context = {
                'file_name': file.file_name,
                'file_size': file.file_size,
                'download_link': file.file.url
            }
            messages.error(request, 'You cannot access the restricted part of this file because you are not the uploader')
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
    return render(request, 'file/download_error.html')