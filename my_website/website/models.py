from django.db import models
import random

from . import functions

# Create your models here.

class Guess(models.Model):
    cows = models.IntegerField()
    bulls = models.IntegerField()
    def __str__(self):
        return f"COWS: {self.cows}, BULLS: {self.bulls}"

#game is finished
class GameFinished(Exception): 
    def __init__(self):
        return

#error in cows and bulls input
class InputError(Exception):
    def __init__(self):
        return

class Try(models.Model):

    def __init__(self, cows, bulls, guess, choices):
        self.cows = cows
        self.bulls = bulls
        self.guess = guess
        self.choices = choices

    def __str__(self):
        return self.guess

    def new_input(self, cows, bulls):
        self.cows = cows
        self.bulls = bulls
        if self.is_correct():
            raise GameFinished
        if (self.cows + self.bulls > 4) or (cows == 3 and bulls == 1):
            raise InputError

    def is_correct(self):
        if int(self.cows) == 4:
            return True
        else:
            return False

    def next_guess(self):
        choices_temp = []
        for choice in self.choices:
            toll = 0
            for i in range(0,4):
                if choice[i] == self.guess[i]:
                    toll = toll + 1
            if toll != self.cows:
                continue
            choices_temp.append(choice)
        choices_temp1 = []
        for choice in choices_temp:
            toll = 0
            for i in range(0,4):
                for j in range(0,4):
                    if i !=j:
                        if choice[i] == self.guess[j]:
                            toll = toll + 1
            if toll != self.bulls:
                continue
            choices_temp1.append(choice)
        if len(choices_temp1) == 0:
            raise InputError
        new_guess = random.choice(choices_temp1)
        return new_guess, choices_temp1

