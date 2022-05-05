from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Genre

def index(request):
    return HttpResponse(serializers.serialize('json', Genre.objects.all()), content_type='application/json')

def detail(request, genre_id):

    if Genre.objects.filter(pk=genre_id).exists():
        genre = Genre.objects.get(pk=genre_id)
        ret = HttpResponse(serializers.serialize("json", [genre]), content_type='application/json')
    else:
        ret =  JsonResponse({'status':404,'message':"user not found"})
    return ret
