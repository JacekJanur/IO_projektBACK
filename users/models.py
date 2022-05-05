from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=200, default=None, blank=True, null=True)
    def __str__(self):
        return self.email
