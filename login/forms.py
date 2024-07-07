"""
This module defines forms used in the 'login' app.

It includes the following form:
    - LoginForm: A form for user login, which includes fields
    for email and password.

Imports:
    - forms: Django's forms module to create and handle forms.
"""

from django import forms


class LoginForm(forms.Form):
    """
    A form for user login, including email and password fields.

    This form is used to authenticate users by collecting their
    email and password.

    Fields:
        email (EmailField): The user's email address, required for login.
        password (CharField): The user's password, required for login.
    """

    email = forms.EmailField()
    password = forms.CharField()
