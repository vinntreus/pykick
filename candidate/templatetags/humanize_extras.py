from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def humanize_words(value):
    return value.capitalize().replace('_', ' ')
