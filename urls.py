from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^(?:home)?$', views.home, name='home'),

    url(r'^emissions/qlggmc$', views.view_show,  name='show'),

    url(r'^direct/?$', views.live_player, name='live'),
    url(r'^direct/?(?P<show>(-|\w)+)$', views.live_page, name='live-page'),

    url(r'^replay(?:/(?P<page>\d+))?/?$', views.replay, name='replay'),

    url(r'^replay/(?P<show>(-|\w)+)/(?P<page>\d+)?/?$', views.replay, name='replay-show'),

    url(r'^discuter/channel/?$', views.channel,  name='channel'),

    url(r'^feeds/cartons.json$', views.export_cartons),

    url(r'^force-404/?', views.force404),
)