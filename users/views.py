from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from .models import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from datetime import date

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.apps import apps

def index(request):
    return HttpResponse(serializers.serialize('json', User.objects.all()), content_type='application/json')

# @api_view(('GET',))
# def detail(request, user_id):

#     if User.objects.filter(pk=user_id).exists():
#         user = User.objects.get(pk=user_id)
#         ret = HttpResponse(serializers.serialize("json", [user]), content_type='application/json')
#     else:
#         ret =  JsonResponse({'status':404,'message':"user not found"})
#     return ret

@api_view(('GET',))
def detail(request, user_id):

    if User.objects.filter(pk=user_id).exists():
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        ret = Response(serializer.data, status= status.HTTP_200_OK)
    else:
        ret =  JsonResponse({'status':404,'message':"user not found"})
    return ret

def reviews(request, user_id):
    if User.objects.filter(pk=user_id).exists():
        reviews = User.objects.get(pk=user_id).reviews()
        ret = HttpResponse(serializers.serialize("json", reviews), content_type='application/json')
    else:
        ret =  JsonResponse({'status':404,'message':"user not found"})
    return ret

@csrf_exempt
def register(request):
    if request.method == "POST":

        if "name" in request.POST and "password" in request.POST and "email" in request.POST:
            hashed_pwd = make_password(request.POST['password'])
            tokenH = make_password(request.POST['email']+date.today().strftime("%d/%m/%Y %H:%M:%S"))
            if not User.ifMailExist(request.POST['email']):
                b = User(name=request.POST['name'], email=request.POST['email'], password=hashed_pwd, token = tokenH)
                b.save()
                ret =  JsonResponse({'status':200, "token":tokenH})
            else:
                ret =  JsonResponse({'status':405,'message':"Email exist"})

        else:
            ret =  JsonResponse({'status':405,'message':"bad data"})
        
    else:
        ret =  JsonResponse({'status':404,'message':"not found"})
    return ret

@api_view(('POST',))
@csrf_exempt
def login(request):
    if "email" in request.POST and "password" in request.POST:
        if User.ifMailExist(request.POST['email']):
            b = User.objects.get(email=request.POST['email'])
            tokenH = make_password(request.POST['email']+date.today().strftime("%d/%m/%Y %H:%M:%S"))
            if check_password(request.POST['password'], b.password):
                ret =  Response({'token': tokenH}, status= status.HTTP_200_OK)
                b.token = tokenH
                b.save()
            else:
                ret = Response({'message': "wrong password"}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            ret =  Response({'message': "no user with this email"}, status= status.HTTP_401_UNAUTHORIZED)
    else:
        ret =  Response({'message': "bad data"}, status= status.HTTP_401_UNAUTHORIZED)
    return ret