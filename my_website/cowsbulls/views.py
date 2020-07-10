from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm

from .models import Game
import random


def rules(request):
    return render(request, 'cowsbulls/rules.html')

def begin_game(request):
    form=GameForm()
    game = Game.objects.create(
        choices = Game.gen_choices(Game),
        guess = random.choice(Game.gen_choices(Game)),
    )
    return render(request, 'cowsbulls/begin.html', {'game': game, 'form': form})

def play_game(request, id):
    game = get_object_or_404(Game, pk=id)
    if request.method == "POST":
        form = GameForm(data=request.POST)
        if form.is_valid():
            next_guess = form.save(commit=False)
            next_guess.choices, next_guess.guess = game.choices, game.guess
            next_guess.save() 
            return redirect('cowsbulls_play', next_guess.id)
    else:
        game.turn(game.cows, game.bulls)
        game.save()
        if game.is_over:
            return redirect('cowsbulls_gameover') 
        if game.input_error:
            return redirect('cowsbulls_error_page', id)
        else: 
            form=GameForm()
            return render(request, 'cowsbulls/begin.html', {'form': form, 'game':game, 'choices': game.choices})

def error_page(request, id):
    games = Game.objects.all()
    return render(request, 'cowsbulls/error_page.html', {'games':games, 'latest_id': id})

def game_over(request):
    Game.objects.all().delete()
    return render(request, 'cowsbulls/game_over.html')
