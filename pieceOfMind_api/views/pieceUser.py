from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from pieceOfMind_api.models import PieceUser

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_objectpermission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class PieceUserViewSet(ViewSet):
  """Request handlers for pieceUser"""
  permission_classes=[ IsOwnerOrReadOnly ]

  def list(self, request):
    pieceUsers = PieceUser.objects.all()
    serializer = PieceUserSerializer(pieceUsers, many=True, context={'request': request})
    return Response(serializer.data)

  def update(self, request, pk=None):
     """Handle PUT requests for a pieceUser"""
     pieceUser = PieceUser.objects.get(user=request.auth.user)
     pieceUser.user.username = request.data['username']
     pieceUser.user.first_name = request.data['first_name']
     pieceUser.user.last_name = request.data['last_name']
     pieceUser.user.email = request.data['email']
     pieceUser.bio = request.data['bio']
     pieceUser.photo = request.data['photo']

     pieceUser.user.save()
     pieceUser.save()

     return Response({}, status=status.HTTP_204_NO_CONTENT)

  def retrieve(self, request, pk=None):
    """Handles GET requests for single pieceUser"""
    try:
      pieceUser = PieceUser.objects.get(pk=pk, user=request.auth.user)
      serializer = PieceUserSerializer(pieceUser, many=False, context={'request': request})
      return Response(serializer.data)
    except PieceUser.DoesNotExist as ex:
      return Response(
        {'message': "The requested user does not exist, or you insufficient permission to access it"},
        status=status.HTTP_404_NOT_FOUND
      )
    except Exception as ex:
      return HttpResponseServerError(ex)

  def destroy(self, request, pk=None):
    try:
      user = User.objects.get(pk=request.auth.user.id)
      self.check_object_permissions(request, user)
      user.delete()

      return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    except PieceUser.DoesNotExist as ex:
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
    url = serializers.HyperlinkedIdentityField(
      view_name='pieceUser',
      lookup_field='id'
    )
    fields = ('id', 'user', 'bio')
    depth = 1
