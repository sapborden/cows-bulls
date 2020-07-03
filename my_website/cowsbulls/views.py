from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm

from .models import Game
import random


def rules(request):
    return render(request, 'cowsbulls/rules.html')

def begin_game(request):
    game = Game.objects.create(
        choices = Game.gen_choices(Game),
        guess = random.choice(Game.gen_choices(Game)),
    )
    form=GameForm()
    return render(request, 'cowsbulls/begin.html', {'game': game, 'form': form})

def play_game(request, id):
    game = get_object_or_404(Game, pk=id)
    if request.method == "POST":
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cowsbulls_play', id)
    else:
        form = GameForm()
#        guess = game.turn(game.cows, game.bulls)
        return render(request, 'cowsbulls/begin.html', {'form': form, 'game':game})
