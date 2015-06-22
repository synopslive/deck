from django import template
from deck.models import Show
from datetime import datetime, date
from math import ceil

register = template.Library()


@register.inclusion_tag('components/header.html')
def header():
    all_shows = Show.objects.filter(archived=False).order_by("category__name", "short")

    hours_left = int(ceil((datetime(2015, 6, 23, 23, 59, 59) - datetime.now()).total_seconds() / 60 / 60))

    return {
        'all_shows': all_shows,
        'hours_left': hours_left
    }
