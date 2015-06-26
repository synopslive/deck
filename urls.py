from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
import views

urlpatterns = patterns(
    '',

    url(r'^(?:home)?$', views.home, name='home'),

    url(r'^decouvrir/emissions$', RedirectView.as_view(url='/', permanent=True), name='shows'),
    # url(r'^decouvrir/grille$', views.planning, name='planning'),

    url(r'^emission/(?P<show>(-|\w)+)$', views.view_show, name='show'),
    url(r'^emission/(?P<show>(-|\w)+)/(?P<page>\d+)?/?', views.view_show, name='show-page'),

    url(r'^direct/?$', views.live_player, name='live'),
    url(r'^direct/(?P<show>(-|\w)+)$', views.live_page, name='live-page'),

    url(r'^replay(?:/(?P<page>\d+))?/?$', RedirectView.as_view(url='/', permanent=True), name='replay'),

    url(r'^replay/(?P<show>(-|\w)+)/(?P<page>\d+)?/?$', views.replay, name='replay-show'),

    url(r'^feeds/cartons\.json$', views.export_cartons),
    url(r'^feeds/current_episode\.json$', views.export_current_episode),
    url(r'^feeds/shows\.json$', views.export_all_shows),

    url(r'^force-404/?', views.force404),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
