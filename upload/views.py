from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import UploadFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploaded_files')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def uploaded_files(request):
    files = UploadFile.objects.all()
    return render(request, 'uploaded_files.html', {'files': files})
