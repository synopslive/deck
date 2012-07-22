from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^(?:home)?$', views.home, name='home'),

    url(r'^emissions/qlggmc$', views.view_show,  name='show'),

    url(r'^ecouter/en-?direct/?$', views.live_player, name='live'),

    url(r'^ecouter/telecharger(?:/(?P<page>\d+))?/?$', views.replay, name='replay'),

    url(r'^ecouter/telecharger/(?P<show>(-|\w)+)/(?P<page>\d+)?/?$', views.replay, name='replay-show'),

    url(r'^discuter/channel/?$', views.channel,  name='channel'),

    url(r'^qlggmc/?', views.only_qlggmc),
    url(r'^respawn/?', views.only_respawn),

    url(r'^.*/', 'deck.views.go404'),
)