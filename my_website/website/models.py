from django.db import models

from . import cowsbulls_comp

# Create your models here.

class Guess(models.Model):
    cows = models.IntegerField()
    bulls = models.IntegerField()
    def __str__(self):
        return f"COWS: {self.cows}, BULLS: {self.bulls}"