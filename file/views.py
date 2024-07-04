from django.shortcuts import render, get_object_or_404
from upload.models import UploadFile

def file(request, file_token):
    file = get_object_or_404(UploadFile, download_link=file_token)
    
    context = {
		'file_name': file.file_name,
		'file_size': file.file_size,
		'download_link': file.file.url
	}
    return render(request, 'file/download.html', context)

def delete(request):
    return render(request, 'file/delete.html')
