from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.generic.base import View
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pieceOfMind_api.models import Room

class RoomSerializer(serializers.HyperlinkedModelSerializer):
  """JSON Serializer for Room"""
  class Meta:
    model = Room
    url = serializers.HyperlinkedIdentityField(
      view_name='room',
      lookup_field='id'
    )
    fields = ('id', 'name')

class RoomViewSet(ViewSet):
  """Request handlers for Rooms"""
  def list(self, request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True, context={"request": request})
    return Response(serializer.data)
