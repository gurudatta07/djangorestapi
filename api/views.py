from django.shortcuts import render
from rest_framework import generics
from .models import Dataset1
from .serializers import Dataset1Serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

class CreateView(generics.ListCreateAPIView):
    queryset = Dataset1
    serializer_class = Dataset1Serializer

@api_view(["POST"])
def Greetings(name):
    try:
        return JsonResponse("Hello "+name.body.decode('ASCII')+" Good Evening!",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
