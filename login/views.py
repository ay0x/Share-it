"""
This module contains views related to user authentication
in the 'login' app.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


def user_login(request):
    """
    Handles user login by processing the login form data
    and authenticating the user.

    If the request method is POST, the function processes
    the submitted form data, authenticates the user, and
    logs them in if credentials are valid. It also handles
    error messages for invalid login attempts.

    If the request method is GET, or the form is invalid,
    it renders the login page with the form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login page with the form
        if GET or form submission fails,or a redirect to
        the dashboard page upon successful login.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #Check if Django form has been submitted with valid data.
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
                return render(request, 'pages/login.html', \
                    {'post_data': request.POST})
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})
