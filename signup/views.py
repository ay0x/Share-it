"""
This module defines the view for user signup in the 'signup' app.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegistrationForm
from shareit.my_utils import generate_token


def signup(request):
    """
    Handle user signup.

    This view handles both GET and POST requests to register a new user.
    It validates the user input using `UserRegistrationForm` and saves
    the user data if the form is valid.

    It also generates a unique ID for the user and provides feedback
    messages to the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered signup page
        or a redirect to the login page.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request,
                           'An account with this email already exists.')
            return render(request,
                          'pages/signup.html', {'post_data': request.POST})

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_unique_gen_id = generate_token(32)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,
                             'Profile created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'pages/signup.html', {'form': form})
