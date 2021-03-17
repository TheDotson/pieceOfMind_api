from rest_framework import serializers
from pieceOfMind_api.models import PieceUser
from django.contrib.auth.models import User

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
        depth = 1

class PieceUserCreateSerializer(serializers.ModelSerializer):
  """JSON serializer for pieceUser"""
  class Meta:
        model = PieceUser
        fields = ('id', 'bio', 'user', 'photo')

class PieceUserUpdateSerializer(serializers.ModelSerializer):
  """JSON serializer for pieceUser"""
  class Meta:
        model = PieceUser
        fields = ('bio', 'user', 'photo')
