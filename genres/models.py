from django.db import models
from rest_framework import serializers

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'