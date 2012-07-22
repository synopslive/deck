from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^(?:home)?$', 'deck.views.home', name='home'),

    url(r'^emissions/qlggmc$', 'deck.views.view_show', name='home'),

    url(r'^ecouter/en-?direct$', 'deck.views.live_player', name='home'),

    url(r'^ecouter/telecharger$', 'deck.views.replay', name='home'),

    url(r'^discuter/channel$', 'deck.views.channel'),

    url(r'^qlggmc/?', 'deck.views.only_qlggmc'),
    url(r'^respawn/?', 'deck.views.only_respawn'),

    url(r'^.*/', 'deck.views.go404'),
)