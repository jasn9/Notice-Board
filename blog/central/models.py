from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200);
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    birth_year = models.IntegerField(default=0)
    affilation = models.CharField(max_length=200)


class Board(models.Model):
    board_id = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Notice(models.Model):
    notice_id = models.CharField(max_length=200)
    board_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField('date published')


class AccessBoard(models.Model):
    board_id = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
