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
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': form})

@login_required(login_url='/login/')
def history(request):
    user_files = request.user.uploadfile_set.all()
    return render(request, 'account/history.html', {'user_files': user_files})

@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('upload_file')
