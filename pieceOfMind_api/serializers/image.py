from rest_framework import serializers
from pieceOfMind_api.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', "image_file")
