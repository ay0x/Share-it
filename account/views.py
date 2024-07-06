from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import ProfileForm

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'pages/home.html')

@login_required(login_url='/login/')
def profile(request):
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
    if request.method == 'POST':
        return redirect('upload_file')
        
    user_files = request.user.uploadfile_set.all()
    return render(request, 'account/history.html', {'user_files': user_files})


@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('upload_file')
