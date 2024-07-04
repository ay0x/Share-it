from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import UploadFile
from signup.models import User

def upload_file(request):
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
                uploaded_file = UploadFile(file=file, upload_by=user if user else None)
                uploaded_file.save()
                print("After save")
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
