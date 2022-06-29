from django.db import models

# Create your models here.


class Hangman(models.Model):
    word = models.CharField(max_length=100)
    tried_chars = models.CharField(max_length=26, blank=True, default="")
    max_try = models.SmallIntegerField(default=7)
