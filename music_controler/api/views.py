from django.shortcuts import render
from rest_framework import generics
from .models import room
from .serelizers import RoomSreilizer
# Create your views here.
class roomView(generics.ListAPIView):
    queryset=room.objects.all()
    serializer_class = RoomSreilizer
