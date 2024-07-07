"""
This module defines a custom user model and its manager for the application.
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the User model.

    This manager provides methods to create regular users and superusers.
    """
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email, full name,
        and password.

        Args:
            email (str): The email address of the user.
            full_name (str): The full name of the user.
            password (str, optional): The password for the user.
            Defaults to None.
            **extra_fields: Additional fields to be included in
            the user record.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If the email is not provided.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None,
                         **extra_fields):
        """
        Creates and saves a superuser with the given email,
        full name, and password.

        Args:
            email (str): The email address of the superuser.
            full_name (str): The full name of the superuser.
            password (str, optional): The password for the superuser.
            Defaults to None.
            **extra_fields: Additional fields to be included
            in the superuser record.

        Returns:
            User: The created superuser object.

        Raises:
            ValueError: If `is_staff` or `is_superuser` are not set to True.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, full_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model extending Django's AbstractBaseUser and PermissionsMixin.
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    primary_use = models.CharField(max_length=255)
    user_unique_gen_id = models.CharField(max_length=32,
                                          editable=False, unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
