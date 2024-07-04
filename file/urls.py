from django.urls import path
from . import views

urlpatterns = [
    path('file/', views.file, name='file'),
    path('file/delete/', views.delete, name='delete'),
]