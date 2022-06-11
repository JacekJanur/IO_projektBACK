from django.shortcuts import render

from .models import Review

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.apps import apps
from django.db.models import Q

@api_view(('POST',))
def add(request):
    if "game" in request.POST and "token" in request.POST and "review" in request.POST:
        user = apps.get_model('users.User').getUserByToken(request.POST['token'])
        try:
            review = float(request.POST['review'])
        except:
            return Response({'message': "review not number"}, status= status.HTTP_401_UNAUTHORIZED)
        if user is not None and apps.get_model('games.Game').objects.filter(pk=request.POST['game']).exists() and 0<=float(request.POST['review'])<=5:
            game = apps.get_model('games.Game').objects.get(pk=request.POST['game'])

            if Review.objects.filter(game=game, user=user).exists():
                r = Review.objects.get(game=game, user=user)
                r.review = review
                r.save()
            else:
                r = Review.objects.create(user = user, game = game, review = review)
                r.save()
            ret =  Response({'message': "ok"}, status= status.HTTP_200_OK)
        else:
            ret =  Response({'message': "bad token or review"}, status= status.HTTP_401_UNAUTHORIZED)
    else:
        ret =  Response({'message': "bad data"}, status= status.HTTP_401_UNAUTHORIZED)
    return ret