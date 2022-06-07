from django.shortcuts import render
from .models import Comment

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