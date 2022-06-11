from django.db import models
from django.apps import apps
from rest_framework import serializers
from reviews.models import ReviewSerializer
from reviews.models import Review
from comments.models import CommentSerializerUser


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=200, default=None, blank=True, null=True)

    
    def __str__(self):
        return '%s %s' % (self.email, self.name)


    def reviews(self):
        return Review.objects.filter(user=self)

    def ifMailExist(email):
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return False
        return True

    def getUserByToken(t):
        try:
            match = User.objects.get(token=t)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return None
        return match

    @property
    def get_reviews(self):
        return self.reviews

class UserSerializer(serializers.ModelSerializer):
    get_comments = CommentSerializerUser(many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'name', "get_comments"]
