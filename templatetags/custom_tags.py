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

@register.simple_tag
def size_unit(value):
    if (value < 1024):
        return f"{value} Bytes"
    elif (value < 1024**2):
        return f"{value / 1024:.2f} KB"
    elif (value < 1024**3):
        return f"{value / 1024**2:.2f} MB"
    elif (value < 1024**4):
        return f"{value / 1024**3:.2f} GB"
    else:
        return f"{value / 1024**4:.2f} TB"


@register.simple_tag(takes_context=True)
def get_host(context):
    request = context['request']
    return request.get_host()

@register.simple_tag(takes_context=True)
def get_full_url(context):
    request = context['request']
    return request.build_absolute_uri('/')
