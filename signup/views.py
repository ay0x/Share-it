from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from shareit.my_utils import generate_token

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_unique_gen_id = generate_token(32)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Profile created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'pages/signup.html')
