from django import template
import string

register = template.Library()


@register.filter
def zeros_to_nines(value):
    if value == '0':
        return '9'
    return value


@register.filter
def only_latin_symbols(value):
    try:
        if value in string.ascii_letters:
            return value
        return ''
    except TypeError:
        return ''
