from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from datetime import date

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