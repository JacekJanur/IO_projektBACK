from django.db import models
from django.apps import apps

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=200, default=None, blank=True, null=True)

    def reviews(self):
        reviews = apps.get_model('reviews.Review')
        return reviews.objects.filter(user=self)

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
