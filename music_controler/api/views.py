from django.shortcuts import render
from rest_framework import generics,status
from .models import room
from .serelizers import RoomSreilizer,CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class roomView(generics.ListAPIView):
    queryset=room.objects.all()
    serializer_class = RoomSreilizer
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.guest_can_pause
            vote_to_skip = serializer.data.votes_to_skip
            host = self.request.session.session_key
            queryset=room.objects.filter(host=host)
            if queryset.exist():
                room=queryset[0]
                room.guest_can_pause=guest_can_pause
                room.vote_to_skip=vote_to_skip
                room.save(update_fields=['guest_can_pause','vote_to_skip'])
                