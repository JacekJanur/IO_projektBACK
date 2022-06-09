from django.shortcuts import render
from .models import Comment

from datetime import date

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.apps import apps

from .models import CommentSerializer


@api_view(('GET',))
def index(request):
    comments=Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(('POST',))
def add(request):
    if "game" in request.POST and "token" in request.POST and "text" in request.POST:
        user = apps.get_model('users.User').getUserByToken(request.POST['token'])
        if user is not None and apps.get_model('games.Game').objects.filter(pk=request.POST['game']).exists():
            game = apps.get_model('games.Game').objects.get(pk=request.POST['game'])
            c = Comment.objects.create(user = user, game = game, text = request.POST['text'], date=date.today().strftime("%Y-%m-%d"))
            c.save()
            ret =  Response({'message': "ok"}, status= status.HTTP_200_OK)
        else:
            ret =  Response({'message': "bad token"}, status= status.HTTP_401_UNAUTHORIZED)
    else:
        ret =  Response({'message': "bad data"}, status= status.HTTP_401_UNAUTHORIZED)
    return ret