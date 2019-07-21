from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE )
    username = models.CharField(max_length=200);
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    birth_year = models.IntegerField(default=0)
    affilation = models.CharField(max_length=200)

    

class Article(models.Model):
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE )
    visible = models.BooleanField(default=True)
    topic = models.CharField(max_length=200)
    article = models.TextField()


