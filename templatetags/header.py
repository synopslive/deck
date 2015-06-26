from django import template
from deck.models import Show
from datetime import datetime, date
from math import ceil

register = template.Library()


@register.inclusion_tag('components/header.html')
def header():
    return {}
