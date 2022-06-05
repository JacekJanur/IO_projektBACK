from django.db import models
from rest_framework import serializers

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    review = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = [['user', 'game']]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'