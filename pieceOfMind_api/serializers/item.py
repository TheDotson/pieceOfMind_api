from rest_framework import serializers
from pieceOfMind_api.models import Item, Room

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
  location = RoomSerializer(read_only=True)
  class Meta:
      model = Item
      fields = ('id', 'name', 'image', 'price', 'location')

class ItemCreateSerializer(serializers.ModelSerializer):
  class Meta:
      model = Item
      fields = ('id', 'name', 'image', 'price', 'location')

class ItemUpdateSerializer(serializers.ModelSerializer):
  class Meta:
      model = Item
      fields = ('name', 'image', 'price', 'location')
