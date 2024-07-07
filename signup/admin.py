"""
This module customizes the Django admin interface for the User model.

It includes custom forms for changing and creating users, and a custom
UserAdmin class that defines how the User model is displayed and managed
in the admin interface.

Imports:
    - admin: Django's admin module for registering models with the admin site.
    - BaseUserAdmin: The default UserAdmin class provided by Django.
    - UserChangeForm, UserCreationForm: Forms for handling user creation
    and modification.
    - User: The custom User model defined in the application's models.

Classes:
    - CustomUserChangeForm: A form for changing user details.
    - CustomUserCreationForm: A form for creating new users.
    - UserAdmin: A custom admin interface for the User model.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating user details.

    This form is based on Django's UserChangeForm and is customized
    to use the custom User model.
    """
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users.

    This form is based on Django's UserCreationForm and is customized to
    use the custom User model.
    The form includes fields for email, full name, and password.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'full_name', 'password1', 'password2')


class UserAdmin(BaseUserAdmin):
    """
    A custom admin interface for the User model.

    This admin class defines how the User model is displayed and managed
    in the Django admin site.
    It includes custom forms for adding and changing users and specifies
    the fields to display, filter, and search in the admin interface.
    """
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'primary_use')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',
                                        'created_on', 'updated_on')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)


admin.site.register(User, UserAdmin)
