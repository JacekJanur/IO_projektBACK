from django.db import models
from genres.models import Genre
from users.models import User

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200, default="default.jpg")