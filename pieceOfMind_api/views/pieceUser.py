from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from pieceOfMind_api.models import PieceUser
from pieceOfMind_api.serializers import *

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_objectpermission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class PieceUserViewSet(viewsets.ModelViewSet):
  """Request handlers for pieceUser"""
  permission_classes=[ IsOwnerOrReadOnly ]
  queryset = PieceUser.objects.all()
  serializer_class = PieceUserSerializer

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from pieceOfMind_api.models import PieceUser
from pieceOfMind_api.serializers import *

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_objectpermission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class PieceUserViewSet(viewsets.ModelViewSet):
  """Request handlers for pieceUser"""
  permission_classes=[ IsOwnerOrReadOnly ]
  queryset = PieceUser.objects.all()
  serializer_class = PieceUserSerializer

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from pieceOfMind_api.models import PieceUser
from pieceOfMind_api.serializers import *

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_objectpermission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class PieceUserViewSet(viewsets.ModelViewSet):
  """Request handlers for pieceUser"""
  permission_classes=[ IsOwnerOrReadOnly ]
  queryset = PieceUser.objects.all()
  serializer_class = PieceUserSerializer

  def create(self, request):
    serializer = PieceUserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

  def update(self, request, pk):
    pieceUser = self.get_object()
    serializer = PieceUserUpdateSerializer(pieceUser, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=HttpResponseBadRequest.status_code)
