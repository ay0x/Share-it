"""
Contains definition to handle request HTTPRequest and returns the
appropriate response
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import ProfileForm
from upload.models import DeletedFile, ExpiredFile, UploadFile


@login_required(login_url='/login/')
def dashboard(request):
    """
    Returns the home page for the dashboard

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page as an HTTP response.
    """
    return render(request, 'pages/home.html')


@login_required(login_url='/login/')
def profile(request):
    """
    Handles the display and update of the user's profile.

    If the request method is POST, it attempts to update the user's full name.
    If successful, it redirects to the profile page with a success message.
    If the full name is not provided, it returns an error message.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page with the user's information.
    """
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        if full_name:
            request.user.full_name = full_name
            request.user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request, 'account/profile.html', {'user': request.user})


@login_required(login_url='/login/')
def history(request):
    """
    Displays the user's file upload history and their statuses.

    If the request method is POST, it redirects to the file upload page.
    Otherwise, it queries the database for the user's files,
    annotates each file with its status, and renders the history
    page with this information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered history page with the user's uploaded
        files and their statuses.
    """
    if request.method == 'POST':
        return redirect('upload_file')

    user = request.user
    # Query all files uploaded by the user
    active_files = UploadFile.objects.filter(upload_by=user)
    deleted_files = DeletedFile.objects.filter(upload_by=user)
    expired_files = ExpiredFile.objects.filter(upload_by=user)

    # Annotate each file with its status
    files_with_status = []
    for file in active_files:
        files_with_status.append({
            'file': file,
            'status': 'Active'
        })
    for file in deleted_files:
        files_with_status.append({
            'file': file,
            'status': 'Deleted'
        })
    for file in expired_files:
        files_with_status.append({
            'file': file,
            'status': 'Expired'
        })
    return render(request, 'account/history.html',
                  {'files_with_status': files_with_status})


@login_required(login_url='/login/')
def logout(request):
    """
    Logs out the user and redirects to the home page with a success message.

    This function calls Django's auth_logout to log out the user,
    adds a success message, and then redirects to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the home page.
    """
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('upload_file')
