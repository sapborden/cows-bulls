from django.urls import path

from .views import *

urlpatterns = [
    path('game',  game, name="game"),
    path('dairies', diaries, name="diaries"),
]