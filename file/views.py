from django.shortcuts import render, get_object_or_404, redirect
from upload.models import UploadFile, DeletedFile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def file(request, file_token):
    file = get_object_or_404(UploadFile, download_link=file_token)
    
    context = {
		'file_name': file.file_name,
		'file_size': file.file_size,
		'download_link': file.file.url
	}
    return render(request, 'file/download.html', context)


@login_required(login_url='/login/')
def user_dl(request, file_token):
    file = get_object_or_404(UploadFile, download_link=file_token)
    
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


def delete(request, file_token):
    file = get_object_or_404(UploadFile, delete_link=file_token)

    if request.method == 'POST':
        # Save file information to DeletedFile model
        DeletedFile.objects.create(
            file_name=file.file_name,
            file_size=file.file_size,
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
