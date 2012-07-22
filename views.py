# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from deck.models import Carton, Episode

def home(request):
    cartons = Carton.objects.filter(visible = True).order_by("episode__time").all()

    has_highlights = Carton.objects.filter(visible = True, highlighted = True).count() > 0

    return render(request, "home.html", {'cartons': cartons, 'has_highlights': has_highlights})

def live_player(request):
    return render(request, "live.html", {})

def channel(request):
    return render(request, "channel.html", {})

def replay(request):
    episodes = Episode.objects.filter(time__lte = datetime.now()).order_by("time").reverse().all()

    return render(request, "replay.html", {'episodes': episodes})

def view_show(request):
    return render(request, "show.html", {})

def only_qlggmc(request):
    return render(request, "events/qlggmc.html", {})

def only_respawn(request):
    return render(request, "events/respawn.html", {})

def go404(request):
    return render(request, "404.html", {})
