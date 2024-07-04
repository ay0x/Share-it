from django import template

register = template.Library()

@register.filter
def first_two_upper(value):
    if isinstance(value, str) and len(value) >= 2:
        return value[:2].upper()
    return value.upper() if isinstance(value, str) else value

@register.filter
def first_name_capitalize(value):
    if isinstance(value, str):
        first_name = value.split()[0]
        return first_name.capitalize()
    return value