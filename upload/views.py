# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .forms import UploadFileForm
# from .models import UploadFile

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             files = request.FILES.getlist('files')
#             for file in files:
#                 uploaded_file = UploadFile(file=file)
#                 uploaded_file.save()
#             return redirect('uploaded_files')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

# def uploaded_files(request):
#     files = UploadFile.objects.all()
#     return render(request, 'uploaded_files.html', {'files': files})
# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import UploadFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('files')
            for file in files:
                uploaded_file = UploadFile(file=file)
                uploaded_file.save()
            #return JsonResponse({'message': 'File(s) uploaded successfully!'})
            return redirect('uploaded_files')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def uploaded_files(request):
    files = UploadFile.objects.all()
    return render(request, 'uploaded_files.html', {'files': files})
