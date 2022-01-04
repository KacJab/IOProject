from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here


class Player(AbstractUser):
    avatar = models.ImageField(default="images/default.png", null=True, blank=True, upload_to="images")
    result_multiplayer = models.PositiveIntegerField(default=0)
    result_easy = models.PositiveIntegerField(default=0)
    result_medium = models.PositiveIntegerField(default=0)
    result_hard = models.PositiveIntegerField(default=0)


class Result (models.Model):
    MODE = (
        ('multiplayer', 'multiplayer'),
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard')
    )
    # player = models.ForeignKey(Player, null=True, related_name='player', on_delete=models.SET_NULL)
    mode = models.CharField(choices=MODE, max_length=20)
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    result1 = models.PositiveIntegerField()
    result2 = models.PositiveIntegerField()
    transcript1 = models.TextField()
    transcript2 = models.TextField()
    # date = models.DateTimeField(auto_now_add=True, null=True)
