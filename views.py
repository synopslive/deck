# Create your views here.
from datetime import datetime, timedelta
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from deck.models import Carton, Episode, Show, LivePage


def home(request):
    cartons = Carton.objects.filter(visible=True).order_by("episode__time").all()

    has_highlights = Carton.objects.filter(visible=True, highlighted=True).count() > 0

    return render(request, "home.html", {'cartons': cartons, 'has_highlights': has_highlights})


def live_player(request):
    try:
        episode = Episode.objects.filter(time__lte=datetime.now() + timedelta(hours=12)) \
            .filter(time__gte=datetime.now() - timedelta(hours=4)) \
            .exclude(termined=True).order_by("time").select_related('show')[0]

        try:
            if episode.show.livepage_url is not None and len(episode.show.livepage_url) > 1:
                return redirect(episode.show.livepage_url)

            if episode.livepage_url is not None and len(episode.livepage_url) > 1:
                return redirect(episode.livepage_url)

            livepage = episode.show.livepage

            if livepage:
                return redirect('live-page', show=episode.show.slug)
        except LivePage.DoesNotExist:
            pass
    except IndexError:
        pass

    return render(request, "live.html", {})


def live_page(request, show):
    show = get_object_or_404(Show, slug=show)
    try:
        page = show.livepage
    except LivePage.DoesNotExist, e:
        raise Http404

    return render(request, "live-page.html", {"show": show, 'page': page})


def channel(request):
    return render(request, "channel.html", {})


def replay(request, page=1, show=None):
    episodes = Episode.objects.filter(time__lte=datetime.now()).select_related('show')
    shows = Show.objects.all()

    if show is not None:
        show = get_object_or_404(Show, slug=show)
        episodes = episodes.filter(show=show)

    episodes = episodes.order_by("time").reverse()

    paged = Paginator(episodes, 10)

    page = request.GET.get('page')
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


def view_show(request):
    return render(request, "show.html", {})


def force404(request):
    return render(request, "404.html", {})


def force500(request):
    return render(request, "500.html", {})


def export_cartons(request):
    cartons = Carton.objects.filter(visible=True) \
        .filter(episode__termined=False) \
        .filter(episode__time__lte=datetime.now() + timedelta(days=45)) \
        .select_related('episode') \
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
