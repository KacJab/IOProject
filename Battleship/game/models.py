from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here


class Player(AbstractUser):
    avatar = models.ImageField(default="images/default.png", null=True, blank=True, upload_to="images")


class Game(models.Model):
    MODE = (
        ('UNDEFINED', 'UNDEFINED'),
        ('EASY', 'EASY'),
        ('MEDIUM', 'MEDIUM'),
        ('HARD', 'HARD')
    )
    mode = models.CharField(choices=MODE, max_length=20, null=True)
    user1 = models.ForeignKey(Player, null=True, related_name='user1', on_delete=models.SET_NULL)
    user2 = models.ForeignKey(Player, null=True, related_name='user2', on_delete=models.SET_NULL)
    user1_result = models.PositiveIntegerField()
    user2_result = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True, null=True)


class Result (models.Model):
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
