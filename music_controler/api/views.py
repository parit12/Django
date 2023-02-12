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
    room.objects.all().delete()
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            vote_to_skip = serializer.data.get('vote_to_skip')
            host = self.request.session.session_key
            queryset=room.objects.filter(host=host)
            if queryset.exists():
                Room=queryset[0]
                Room.guest_can_pause=guest_can_pause
                Room.vote_to_skip=vote_to_skip
                Room.save(update_fields=['guest_can_pause','vote_to_skip'])
                print("hello")
                return Response(RoomSreilizer(Room).data, status=status.HTTP_200_OK)
            else:
                Room=room(host=host,guest_can_pause=guest_can_pause,vote_to_skip=vote_to_skip)
                Room.save()
                return Response(RoomSreilizer(Room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
