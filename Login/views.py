from django.shortcuts import render
from rest_framework import viewsets
from .models import Login
from .serializers import loginserializer

# Create your views here.
class loginview(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = loginserializer