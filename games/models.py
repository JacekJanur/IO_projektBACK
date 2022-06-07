from django.db import models
from genres.models import Genre
from users.models import User
from django.apps import apps
from rest_framework import serializers
from itertools import chain
from comments.models import CommentSerializer
from comments.models import Comment

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200, default="default.jpg")
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.jpg')

    def reviews(self):
        reviews = apps.get_model('reviews.Review')
        return reviews.objects.filter(game=self)

    @property
    def avg(self):
        reviews = apps.get_model('reviews.Review').objects.filter(game=self)
        suma = 0
        for review in reviews:
            suma += review.review
        return 0 if len(reviews) == 0 else suma/len(reviews)

class GameSerializerAvg(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['avg'] = instance.avg

        return representation

class GameSerializerComments(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Game
        fields = ['id', 'description', 'genre', 'name','comments']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['avg'] = instance.avg

        return representation