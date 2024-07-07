"""
This module defines custom template filters and tags for use in
Django templates.
"""
from django import template

register = template.Library()


@register.filter
def first_two_upper(value):
    """
    Converts the first two characters of a string to uppercase.

    Args:
        value (str): The string to process.

    Returns:
        str: The processed string with the first two characters in uppercase.
    """
    if isinstance(value, str) and len(value) >= 2:
        return value[:2].upper()
    return value.upper() if isinstance(value, str) else value


@register.filter
def first_name_capitalize(value):
    """
    Capitalizes the first name in a string.

    Args:
        value (str): The string to process.

    Returns:
        str: The first name capitalized.
    """
    if isinstance(value, str):
        first_name = value.split()[0]
        return first_name.capitalize()
    return value


@register.simple_tag
def size_unit(value):
    """
    Converts a file size in bytes to a human-readable format.

    Args:
        value (int): The file size in bytes.

    Returns:
        str: The file size in a human-readable format (Bytes, KB, MB, GB, TB).
    """
    if value < 1024:
        return f"{value} Bytes"
    elif value < 1024**2:
        return f"{value / 1024:.2f} KB"
    elif value < 1024**3:
        return f"{value / 1024**2:.2f} MB"
    elif value < 1024**4:
        return f"{value / 1024**3:.2f} GB"
    else:
        return f"{value / 1024**4:.2f} TB"


@register.simple_tag(takes_context=True)
def get_host(context):
    """
    Retrieves the host of the current request.

    Args:
        context (dict): The template context.

    Returns:
        str: The host of the current request.
    """
    request = context['request']
    return request.get_host()


@register.simple_tag(takes_context=True)
def get_full_url(context):
    """
    Retrieves the full URL of the current request.

    Args:
        context (dict): The template context.

    Returns:
        str: The full URL of the current request.
    """
    request = context['request']
    return request.build_absolute_uri('/')
