from django.urls import path

from .views import *

urlpatterns = [
    path('game_start',  game_start, name="game_start"),
    path('dairies', diaries, name="diaries"),
    path('play_game', play_game, name="play_game"),
]