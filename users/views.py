from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User

def index(request):
    return HttpResponse(serializers.serialize('json', User.objects.all()), content_type='application/json')

def detail(request, user_id):

    if User.objects.filter(pk=user_id).exists():
        user = User.objects.get(pk=user_id)
        ret = HttpResponse(serializers.serialize("json", [user]), content_type='application/json')
    else:
        ret =  JsonResponse({'status':404,'message':"user not found"})
    return ret

def reviews(request, user_id):
    if User.objects.filter(pk=user_id).exists():
        reviews = User.objects.get(pk=user_id).reviews()
        ret = HttpResponse(serializers.serialize("json", reviews), content_type='application/json')
    else:
        ret =  JsonResponse({'status':404,'message':"reviews not found"})
    return ret