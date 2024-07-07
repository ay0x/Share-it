"""
This module defines the form used for user registration
in the 'signup' application.

The UserRegistrationForm class extends Django's ModelForm
to include additional fields for password and password confirmation,
along with custom validation to ensure the passwords match.
"""

from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    """
    A form for registering new users.

    This form extends Django's ModelForm and includes additional
    fields for password and password confirmation. It also
    includes custom validation to ensure the passwords match.

    Fields:
        - full_name: The full name of the user.
        - email: The email address of the user.
        - password: The password for the user, rendered as a
        password input.
        - confirm_password: A field to confirm the password,
        rendered as a password input.
        - primary_use: The primary use of the account.

    Methods:
        - clean: Custom validation method to ensure the passwords match.
    """
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'primary_use']

    def clean(self):
        """
        Custom validation method to ensure the passwords match.

        This method overrides the default clean method to add additional
        validation to check that the password and confirm_password fields
        match. If they do not match,a ValidationError is raised.

        Returns:
            dict: The cleaned data.

        Raises:
            forms.ValidationError: If the passwords do not match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
