from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from pieceOfMind_api.models import *
from pieceOfMind_api.serializers import *

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_objectpermission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class CollectionViewSet(viewsets.ModelViewSet):
  """Request handlers for collection"""
  permission_classes=[ IsOwnerOrReadOnly ]
  queryset = Collection.objects.all()
  serializer_class = CollectionSerializer

  def create(self, request):
    serializer = CollectionCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

  def update(self, request, pk):
    collection = self.get_object()
    serializer = CollectionUpdateSerializer(collection, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

  def destroy(self, request, pk=None):
    try:
      collection = Collection.objects.get(pk=pk)
      self.check_object_permissions(request, collection)
      collection.delete()

      return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    except Collection.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
