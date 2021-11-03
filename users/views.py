from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
from .serializers import *
# Create your views here.

class Users(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()