from django.contrib import admin

from .models import Game, Choice, Guess

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display=('id', 'first_player', 'second_player', 'status')
    

admin.site.register(Choice)
admin.site.register(Guess)