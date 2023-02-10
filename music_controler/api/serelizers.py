from rest_framework import serializers
from .models import room

class RoomSreilizer(serializers.ModelSerializer):
    class Meta:
        model=room
        fields=('id','code','host','guest_can_pause','vote_to_skip','create_at')

class CreateRoomSerializer(serializers.ModelSerilizer):
    class Meta:
        model=room
        fields=('guest_can_pause','vote_to_skip')