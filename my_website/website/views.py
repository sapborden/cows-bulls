from django.shortcuts import render, get_object_or_404, redirect

from django.forms import modelform_factory

from .models import Guess

from .cowsbulls_comp import *

# Create your views here.

def welcome(request):
    return render(request, "website/index.html")

GuessForm = modelform_factory(Guess, exclude=[])

def game(request):
    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("game")
    else:
        form = GuessForm()
    return render(request, "website/game.html", {"form": form, "guess": guess(gen_choices())})

def diaries(request):
    return render(request, "website/DIARIES.html")