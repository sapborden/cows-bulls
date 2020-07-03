from django.conf.urls import url, include

from .views import begin_game, rules, play_game

urlpatterns = [
    url('rules', rules, name="rules"),
    url('begin', begin_game, name="cowsbulls_begin"),
    url('play/(?P<id>\d+)/$', play_game, name="cowsbulls_play")
]