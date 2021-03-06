from django.db import models
import random
from django.contrib.auth.models import User
from django.core.validators import int_list_validator

class PrevGuess(models.Model):
    cows = models.CharField(max_length=1)
    bulls = models.CharField(max_length=1)
    guess = models.CharField(max_length=4)
    choices = models.CharField(validators=[int_list_validator],max_length=20000)

class Game(models.Model):
    cows = models.CharField(max_length=1)
    bulls = models.CharField(max_length=1)
    guess = models.CharField(max_length=4)
    choices = models.CharField(validators=[int_list_validator],max_length=20000)
    is_over = models.BooleanField(default=False, editable=False)
    input_error = models.BooleanField(default=False, editable=False)

    def get_absolute_url(self):
        return reverse('gameplay_detail', args={self.id})

    def gen_choices(self):
        self.choices = []
        for i in range(1,10):
            for j in range(1,10):
                if i != j:
                    for k in range(1,10):
                        if k not in [i,j]:
                            for l in range(1,10):
                                if l not in [i,j,k]:
                                    guess = str(i)+str(j)+str(k)+str(l)
                                    self.choices.append(guess)
        return self.choices

    def _convert_list(self,choices):
        choices = choices.replace("'","")
        choices = choices.replace(" ","")
        choices = choices.strip("\[")
        choices = choices.strip("\]")
        choices = choices.split(",")
        return choices
    
#updates choices and guess
    def turn(self, cows, bulls):
        self.cows = cows
        self.bulls = bulls

        if self.cows == '4':
            self.is_over=True
        else:
            choices_temp = []
            choices = self._convert_list(self.choices)
            for choice in choices:
                toll = 0
                for i in range(0,4):
                    if choice[i] == self.guess[i]:
                        toll = toll + 1
                if str(toll) != self.cows:
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
                if str(toll) != self.bulls:
                    continue
                choices_temp1.append(choice)
            if len(choices_temp1) == 0:
                self.input_error = True
            else:
                self.choices = choices_temp1
                self.guess = random.choice(self.choices)