from django.urls import path
from . import views

urlpatterns = [
    path('file/<str:file_token>', views.file, name='file'),
    path('file/user/dl/<str:file_token>', views.user_dl, name='user_dl'),
    path('file/delete/<str:file_token>', views.delete, name='delete'),
]