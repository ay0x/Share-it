from django.shortcuts import render

def file(request):
    return render(request, 'file/download.html')

def delete(request):
    return render(request, 'file/delete.html')
