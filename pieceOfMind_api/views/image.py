from rest_framework import viewsets, parsers
from pieceOfMind_api.models import Image
from pieceOfMind_api.serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
  parser_classes = [parsers.MultiPartParser]  
  queryset = Image.objects.all()
  serializer_class = ImageSerializer
