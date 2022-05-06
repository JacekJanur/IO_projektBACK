from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Game


def index(request):

    return HttpResponse(serializers.serialize('json', Game.objects.all()), content_type='application/json')

def detail(request, game_id):
    if Game.objects.filter(pk=game_id).exists():
        game = Game.objects.get(pk=game_id)
        ret = HttpResponse(serializers.serialize("json", [game]), content_type='application/json')
    else:
        ret =  JsonResponse({'status':404,'message':"game not found"})
    return ret

def reviews(request, game_id):
    if Game.objects.filter(pk=game_id).exists():
        reviews = Game.objects.get(pk=game_id).reviews()
        ret = HttpResponse(serializers.serialize("json", reviews), content_type='application/json')
    else:
        ret =  JsonResponse({'status':404,'message':"reviews not found"})
    return ret