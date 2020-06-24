from django.db import models
import random
from django.contrib.auth.models import User

GAME_STATUS_CHOICES = (
    ('F', 'First Player Turn'),
    ('S', 'Second Player Turn'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
)

class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    def __str__(self):
        return "{0} vs {1}".format(self.first_player,self.second_player)

#table of choices
class Choice(models.Model):

    choice = models.CharField(max_length=4)

class Guess(models.Model):
    guess = models.CharField(max_length=4)

class UserTurn(models.Model):
    cows = models.IntegerField()
    bulls = models.IntegerField()
    choices = models.ForeignKey(Choice, on_delete=models.CASCADE)
    guess = models.ForeignKey(Guess, on_delete=models.CASCADE)
    count = models.IntegerField()

    game=models.ForeignKey(Game, on_delete=models.CASCADE)