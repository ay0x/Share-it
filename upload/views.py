from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import UploadFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('files')
            token_list = []
            file_list = []
            for file in files:
                uploaded_file = UploadFile(file=file)
                uploaded_file.save()
                token_list.append(uploaded_file.download_link)
                file_list.append({
                    'file_name': uploaded_file.file_name,
                    'file_size': uploaded_file.file_size,
                    'download_link': uploaded_file.download_link,
                    'delete_link': uploaded_file.delete_link
                })
            return JsonResponse({
                'show_dropbox': False,
                'show_download_list': True,
                'files': file_list
            })
    else:
        return render(request, 'pages/home.html')
        
    # return render(request, 'upload.html', {'form': form})

# def uploaded_files(request):
#     files = UploadFile.objects.all()
#     return render(request, 'uploaded_files.html', {'files': files})
