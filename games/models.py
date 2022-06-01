from django.db import models
from genres.models import Genre
from users.models import User
from django.apps import apps

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200, default="default.jpg")

    def reviews(self):
        reviews = apps.get_model('reviews.Review')
        return reviews.objects.filter(game=self)


