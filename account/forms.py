"""
This module defines forms used in the application.
"""
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileForm(forms.ModelForm):
    """
    A form for updating the user's profile information.

    This form allows users to update their full name.
    It uses Django's ModelForm to automatically generate form fields
    based on the User model.

    Attributes:
        model (User): The user model being used in the project.
        fields (list): The list of fields to include in the form.
    """
    class Meta:
        model = User
        fields = ['full_name']
