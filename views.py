# Create your views here.
from datetime import datetime
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
    query = Episode.objects.filter(time__lte = datetime.now())
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

def go404(request):
    return render(request, "404.html", {})
