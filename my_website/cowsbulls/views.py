from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm

from .models import Game, PrevGuess
import random


def rules(request):
    return render(request, 'cowsbulls/rules.html')

def begin_game(request):
    Game.objects.all().delete()
    PrevGuess.objects.all().delete()
    form=GameForm()
    game = Game.objects.create(
        choices = Game.gen_choices(Game),
        guess = random.choice(Game.gen_choices(Game)),
    )
    return render(request, 'cowsbulls/begin.html', {'game': game, 'form': form})

def play_game(request, id):
    game = get_object_or_404(Game, pk=id)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            PrevGuess.objects.create(
                cows = game.cows,
                bulls = game.bulls,
                guess = game.guess,
                choices = game.choices
            )
            game.save() 
            return redirect('cowsbulls_play', game.id)
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
    prev_guesses = PrevGuess.objects.all()
    return render(request, 'cowsbulls/error_page.html', {'turns': prev_guesses})

def revert_game(request, id):
    game = Game.objects.get()
    game.input_error=False
    turn = PrevGuess.objects.all()[int(id)-1]
    count = PrevGuess.objects.all().count()
    game.choices, game.guess = turn.choices, turn.guess
    game.save()
    #delete the relevant PrevGuess objects 
    form=GameForm()
    return render(request, 'cowsbulls/begin.html', {'game': game, 'form': form})

def game_over(request):
    return render(request, 'cowsbulls/game_over.html')
