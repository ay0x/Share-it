from django.shortcuts import render, get_object_or_404
from upload.models import UploadFile
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


def delete(request):
    return render(request, 'file/delete.html')
