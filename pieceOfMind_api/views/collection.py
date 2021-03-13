from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from pieceOfMind_api.models import *

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_objectpermission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class CollectionViewSet(ViewSet):
  """Request handlers for collection"""
  permission_classes=[ IsOwnerOrReadOnly ]

  def list(self, request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True, context={'request': request})
    return Response(serializer.data)

  def update(self, request, pk=None):
     """Handle PUT requests for a collection"""
     collection = Collection.objects.get(user=request.auth.user)
     collection.name = request.data['name']

     collection.save()

     return Response({}, status=status.HTTP_204_NO_CONTENT)

  def retrieve(self, request, pk=None):
    """Handles GET requests for single collection"""
    try:
      collection = Collection.objects.get(pk=pk)
      serializer = CollectionSerializer(collection, many=False, context={'request': request})
      return Response(serializer.data)
    except Collection.DoesNotExist as ex:
      return Response(
        {'message': "The requested user does not exist, or you insufficient permission to access it"},
        status=status.HTTP_404_NOT_FOUND
      )
    except Exception as ex:
      return HttpResponseServerError(ex)

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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class PieceUserSerializer(serializers.HyperlinkedModelSerializer):
  """JSON serializer for pieceUser"""
  user = UserSerializer(many=False)
  class Meta:
    model = PieceUser
    # url = serializers.HyperlinkedIdentityField(
    #   view_name='pieceUser',
    #   lookup_field='id'
    # )
    fields = ('id', 'user')
    depth = 1

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'location', 'price')

class CollectionSerializer(serializers.ModelSerializer):
    user = PieceUserSerializer(many=False)
    class Meta:
        model = Collection
        fields = ('id', 'name', 'user')
