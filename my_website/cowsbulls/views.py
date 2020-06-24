from django.shortcuts import render
from .models import Game

def start_game(request):

    num_of_games = len(Game.objects.all())

    return render(request, 'cowsbulls/cowsbulls.html', {'games': num_of_games})
