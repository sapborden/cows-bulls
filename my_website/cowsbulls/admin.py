from django.contrib import admin

from .models import Game, PrevGuess 

# Register your models here.

admin.site.register(PrevGuess)
admin.site.register(Game)