from django.db import models
from rest_framework import serializers
from django.apps import apps

class Comment(models.Model):
    user = models.ForeignKey('users.User',related_name='get_comments', on_delete=models.CASCADE)
    game = models.ForeignKey('games.Game',related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return 'User: %s Game: %s Text: %s' % (self.user, self.game, self.text)

    @property
    def username(self):
        users = apps.get_model('users.User').objects.get(pk=self.user.pk)
        return users.name

    @property
    def gamename(self):
        game = apps.get_model('games.Game').objects.get(pk=self.user.pk)
        return game.name

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.username
        return representation

class CommentSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("text", "date")
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['gamename'] = instance.gamename
        return representation