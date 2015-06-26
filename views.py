from datetime import datetime, timedelta, time
import json
import re
import urllib2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import force_unicode
import markdown2
from deck.models import Episode, Show
import random
import redis

LIVE_HOSTS = ["live.synopslive.net:8000"]
redis_instance = redis.StrictRedis()


def home(request):
    all_shows = Show.objects.order_by("short")

    return render(request, "home.html", {
        'all_shows': all_shows
    })


def planning(request):
    monday = datetime.today().date() - timedelta(days=datetime.today().weekday())
    episodes = Episode.objects.filter(
        time__gte=datetime.combine(monday, time(0,0)),
        time__lt=datetime.combine(monday + timedelta(days=7*4), time(0, 0))
    ).order_by("time")

    return render(request, "planning.html", {
        'episodes': episodes,
        'days': [monday + timedelta(days=i) for i in range(7*4)]
    })


def live_player(request):
    hosts = LIVE_HOSTS[:]

    random.shuffle(hosts)

    return render(request, "live.html", {
        'hosts': hosts
    })


def live_page(request, show):
    show = get_object_or_404(Show, slug=show)

    return redirect('show', show=show.slug)


def replay(request, show, page=1):
    episodes = Episode.objects.filter(time__lte=datetime.now()).select_related('show')
    shows = Show.objects.all()

    show = get_object_or_404(Show, slug=show)
    episodes = episodes.filter(show=show)

    episodes = episodes.order_by("time").reverse()

    paged = Paginator(episodes, 10)

    try:
        current_page_episodes = paged.page(page)
    except PageNotAnInteger:
        current_page_episodes = paged.page(1)
    except EmptyPage:
        current_page_episodes = paged.page(paged.num_pages)

    return render(request, "replay.html", {
        'episodes': current_page_episodes,
        'shows': shows,
        'current_show': show,
        'total': episodes.count()
    })


def view_show(request, show, page=1):
    show = get_object_or_404(Show, slug=show)
    episodes = Episode.objects.select_related('show').filter(show=show).filter(time__lte=datetime.now())\
        .order_by("time").reverse()

    paged = Paginator(episodes, 10)

    try:
        current_page_episodes = paged.page(page)
    except PageNotAnInteger:
        current_page_episodes = paged.page(1)
    except EmptyPage:
        current_page_episodes = paged.page(paged.num_pages)

    return render(request, "show.html", {
        'show': show,
        'episodes': current_page_episodes
    })


def list_shows(request):
    shows = Show.objects.all().order_by("archived", "short")

    return render(request, "shows.html", {"all_shows": shows})


def force404(request):
    return render(request, "404.html", {})


def force500(request):
    return render(request, "500.html", {})


def export_all_shows(request):
    shows = Show.objects.order_by("short")

    response = {}

    for show in shows:
        response[show.id] = {
            "name": show.name,
            "average_duration": show.average_duration
        }

    return HttpResponse(json.dumps(response), content_type="application/json")


def export_current_episode(request):
    cached = redis_instance.get('deck_current_episode_cache')

    if not cached:
        with redis_instance.lock('deck_current_episode_lock'):
            cached = redis_instance.get('deck_current_episode_cache')

            if not cached:
                episodes = Episode.objects.filter(shown=True) \
                    .filter(end_time__gte=datetime.now()) \
                    .select_related('show') \
                    .order_by("time")

                response = {}

                if episodes.count() > 0:
                    episode = episodes[0]
                    response = {
                        'id': episode.id,
                        'bg_image': episode.auto_livepage_bg_image.url,
                        'show_name': episode.show.name,
                        'show_slug': episode.show.slug,
                        'twitter_button_label': episode.show.twitter_button_label,
                        'twitter_button_message': episode.show.twitter_button_message,
                        'twitter_widget': episode.show.twitter_widget,
                        'number': episode.number,
                        'content': markdown2.markdown(force_unicode(episode.content)),
                        'copyright': markdown2.markdown(force_unicode(episode.show.copyright)),
                        'time': episode.time.isoformat(),
                        'end_time': episode.end_time.isoformat()
                    }

                prog = re.compile(r'^mount=.+?, artist=(?P<artist>.*?), title=(?P<title>.*?), listeners=(?P<listeners>.*?)$')

                try:
                    hosts = LIVE_HOSTS[:]
                    random.shuffle(hosts)
                    content = urllib2.urlopen("http://{}/status4.xsl".format(hosts[0]), timeout=2).readlines()
                    interesting_line = [prog.match(line) for line in content if line.startswith("mount=/synopslive-permanent.ogg")][0]

                    response["artist"] = interesting_line.group("artist")
                    response["title"] = interesting_line.group("title")
                except Exception:
                    pass

                cached = json.dumps(response)

                redis_instance.set("deck_current_episode_cache", cached)
                redis_instance.expire("deck_current_episode_cache", 10)

    return HttpResponse(cached, content_type="application/json")


def export_cartons(request):
    episodes = Episode.objects.filter(shown=True) \
        .filter(end_time__gt=datetime.now()) \
        .filter(time__lte=datetime.now() + timedelta(days=3)) \
        .select_related('show') \
        .order_by("time") \
        .all()

    result = []

    for episode in episodes:
        result.append({
            'id': episode.id,
            'bg_image': episode.auto_carton_image.url,
            'show_id': episode.show.id,
            'show_name': episode.show.name,
            'show_slug': episode.show.slug,
            'episode_time': episode.time.isoformat(),
            'episode_number': episode.number,
            'episode_content': unicode(episode.content),
            'episode_summary': episode.summary,
            'livepage_url': reverse('show', args=(episode.show.slug,)),
        })

    return HttpResponse(json.dumps(result), content_type="application/json")
