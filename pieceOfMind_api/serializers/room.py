from rest_framework import serializers
from pieceOfMind_api.models import Room

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'name', 'user')
