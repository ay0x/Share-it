# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload/', views.upload_file, name='upload_file'),
#     path('uploaded_files/', views.uploaded_files, name='uploaded_files'),
# ]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('uploaded_files/', views.uploaded_files, name='uploaded_files'),
]
