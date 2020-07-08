from django.conf.urls import url, include

from .views import begin_game, rules, play_game, game_over

urlpatterns = [
    url('rules', rules, name="cowsbulls_rules"),
    url('begin', begin_game, name="cowsbulls_begin"),
    url('play/(?P<id>\d+)/$', play_game, name="cowsbulls_play"),
    url('game_over', game_over, name="cowsbulls_gameover")
]