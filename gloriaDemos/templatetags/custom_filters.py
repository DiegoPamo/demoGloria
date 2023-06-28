from django import template

register = template.Library()

@register.filter
def cycle_range(value, arg):
    return range(arg - value % arg)