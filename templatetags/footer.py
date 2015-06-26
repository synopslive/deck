from django import template
from deck.models import Show

register = template.Library()


@register.inclusion_tag('components/footer.html')
def footer():
    all_shows = Show.objects.order_by("short")

    return {
        'all_shows': all_shows
    }
