from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("elo")