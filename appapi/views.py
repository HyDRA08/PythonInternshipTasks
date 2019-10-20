from django.shortcuts import render
from rest_framework import generics
from .import serializers
from .models import todo
# Create your views here.
class Listtodo(generics.ListCreateAPIView):
    queryset=todo.objects.all()
    serializer_class=serializers.todoserializers

class Detailname(generics.RetrieveUpdateDestroyAPIView):
    queryset=todo.objects.all()
    serializer_class=serializers.todoserializers