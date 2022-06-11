from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Game
from .models import GameSerializerAvg
from .models import GameSerializerComments
from reviews.models import ReviewSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.apps import apps

@api_view(('GET',))
def index(request):
    games=Game.objects.all()
    serializer = GameSerializerAvg(games, many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(('GET',))
def detail(request, game_id):
    if Game.objects.filter(pk=game_id).exists():
        game = Game.objects.get(pk=game_id)
        serializer = GameSerializerComments(game)
        ret = Response(serializer.data, status= status.HTTP_200_OK)
    else:
        ret = Response({'message':"game not found"}, status= status.HTTP_404_NOT_FOUND)
    return ret

@api_view(('GET',))
def search(request, game_search):
    nothing = True
    if Game.objects.filter(name__icontains=game_search).exists():
        games = Game.objects.filter(name__icontains=game_search)
        serializer = GameSerializerAvg(games, many=True)
        ret = Response(serializer.data, status= status.HTTP_200_OK)
        nothing = False

    else:
        ret = Response({'message':"games not found"}, status= status.HTTP_404_NOT_FOUND)

    return ret





@api_view(('GET',))
def reviews(request, game_id):
    if Game.objects.filter(pk=game_id).exists():
        reviews = Game.objects.get(pk=game_id).reviews()
        serializer = ReviewSerializer(reviews, many=True)
        ret = Response(serializer.data, status= status.HTTP_200_OK)
    else:
        ret = Response({'message':"review not found"}, status= status.HTTP_404_NOT_FOUND)
    return ret

@api_view(('GET',))
def image(request, game_id):
    if Game.objects.filter(pk=game_id).exists():
        image = Game.objects.get(pk=game_id).image
        ret = HttpResponse(image, content_type="image/png")
    else:
        ret = Response({'message':"game not found"}, status= status.HTTP_404_NOT_FOUND)
    return ret