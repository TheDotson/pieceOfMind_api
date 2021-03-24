from django.db import models
from django.db.models.deletion import CASCADE

class Image(models.Model):
    image_file = models.FileField(upload_to='pics/')
