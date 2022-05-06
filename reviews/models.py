from django.db import models

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    review = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = [['user', 'game']]
