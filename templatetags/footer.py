from django import template
from deck.models import Show

register = template.Library()


@register.inclusion_tag('components/footer.html')
def footer():
    random_shows = Show.objects.filter(archived=False).order_by('?')[0:6]
    return {
        'random_shows': random_shows
    }