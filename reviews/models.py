# from django.db import models
# from users.models import User
# from games.models import Game

# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     review = models.IntegerField(max_length=1, blank=True, null=True)

#     class Meta:
#         unique_together = [['user', 'game']]
