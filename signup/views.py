from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserRegistrationForm()
    
    return render(request, 'pages/signup.html')
