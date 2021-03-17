from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.generic.base import View
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from pieceOfMind_api.models import Item
from pieceOfMind_api.serializers import *

class ItemViewSet(viewsets.ModelViewSet):
  """Request handlers for Rooms"""
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

  def create(self, request):
    serializer = ItemCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

  def update(self, request, pk):
    item = self.get_object()
    serializer = ItemUpdateSerializer(item, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=HttpResponseBadRequest.status_code)
