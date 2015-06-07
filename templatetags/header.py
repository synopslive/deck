from django import template
from deck.models import Show
from datetime import datetime, date

register = template.Library()


@register.inclusion_tag('components/header.html')
def header():
    all_shows = Show.objects.filter(archived=False).order_by("category__name", "short")

    days_left = (datetime(2015, 6, 23).date() - date.today()).days

    return {
        'all_shows': all_shows,
        'days_left': days_left
    }
