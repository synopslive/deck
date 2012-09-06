# Create your views here.
from datetime import datetime, timedelta
import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from deck.models import Carton, Episode, Show

def home(request):
    cartons = Carton.objects.filter(visible = True).order_by("episode__time").all()

    has_highlights = Carton.objects.filter(visible = True, highlighted = True).count() > 0

    return render(request, "home.html", {'cartons': cartons, 'has_highlights': has_highlights})

def live_player(request):
    return render(request, "live.html", {})

def channel(request):
    return render(request, "channel.html", {})

def replay(request, page=1, show=None):
    query = Episode.objects.filter(time__lte = datetime.now()).select_related('show')
    shows = Show.objects.all()

    if show is not None:
        show = get_object_or_404(Show, slug=show)
        query = query.filter(show = show)

    episodes = query.order_by("time").reverse().all()

    return render(request, "replay.html", {'episodes': episodes, 'shows': shows, 'current_show': show})

def view_show(request):
    return render(request, "show.html", {})

def only_qlggmc(request):
    return render(request, "events/qlggmc.html", {})

def only_respawn(request):
    return render(request, "events/respawn.html", {})

def force404(request):
    return render(request, "404.html", {})


def export_cartons(request):
    cartons = Carton.objects.filter(visible = True)\
                            .filter(episode__termined = False) \
                            .filter(episode__time__lte = datetime.now() + timedelta(days = 3))\
                            .select_related('episode')\
                            .select_related('show') \
                            .order_by("episode__time") \
                            .all()

    result = []

    # Custom serializing
    # TODO: Use some formatter to relocate that code
    for carton in cartons:
        result.append({
            'id': carton.id,
            'bg_image': carton.bg_image.url,
            'show_id': carton.episode.show.id,
            'show_name': carton.episode.show.name,
            'show_slug': carton.episode.show.slug,
            'episode_time': carton.episode.time.isoformat(),
            'episode_number': carton.episode.number,
            'episode_content': unicode(carton.episode.content),
            'episode_summary': carton.episode.summary,
            'livepage_url': carton.episode.livepage_url,
        })

    return HttpResponse(json.dumps(result))
