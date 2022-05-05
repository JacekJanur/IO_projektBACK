from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import User

def index(request):
    return HttpResponse(serializers.serialize('json', User.objects.all()))
