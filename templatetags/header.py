from django import template
from deck.models import Show

register = template.Library()


@register.inclusion_tag('components/header.html')
def header():
    all_shows = Show.objects.filter(archived=False).order_by("category__name", "short")
    return {
        'all_shows': all_shows
    }