from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.generic.base import View
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers, status
from pieceOfMind_api.models import Room
from pieceOfMind_api.serializers import *

class RoomViewSet(viewsets.ModelViewSet):
  """Request handlers for Rooms"""
  queryset = Room.objects.all()
  serializer_class = RoomSerializer

  def get_queryset(self):
    user = self.request.query_params.get('user', None)
    if user:
      return self.queryset.filter(user=user)
    else:
      return self.queryset
