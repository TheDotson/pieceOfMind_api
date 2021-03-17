from rest_framework import serializers
from django.contrib.auth.models import User
from pieceOfMind_api.models import Collection, Item, PieceUser, Room

class UserSerializer(serializers.ModelSerializer):
  """JSON serializer for user"""
  class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class PieceUserSerializer(serializers.ModelSerializer):
  """JSON serializer for pieceUser"""
  user = UserSerializer(read_only=True)
  class Meta:
        model = PieceUser
        fields = ('id', 'bio', 'user', 'photo')

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
  location = RoomSerializer(read_only=True)
  class Meta:
      model = Item
      fields = ('id', 'name', 'image', 'price', 'location')

class CollectionSerializer(serializers.ModelSerializer):
    user = PieceUserSerializer(read_only=True)
    items = ItemSerializer(read_only=True, many=True)
    class Meta:
        model = Collection
        fields = ('id', 'name', 'user', 'items')

class CollectionCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields = ('id', 'name', 'user', 'items')

class CollectionUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields = ('name', 'user', 'items')
