from django.db import models
from rest_framework import serializers

class Review(models.Model):
    user = models.ForeignKey('users.User', related_name='get_reviews' , on_delete=models.CASCADE)
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    review = models.FloatField(blank=True, null=True)

    def __str__(self):
        return 'User: %s Game: %s Review: %s' % (self.user, self.game, self.review)


    class Meta:
        unique_together = [['user', 'game']]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'