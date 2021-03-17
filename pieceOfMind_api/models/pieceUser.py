from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class PieceUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  photo = models.ImageField(upload_to="pieceUsers", height_field=None, width_field=None, max_length=None, null=True)
  bio = models.CharField(max_length=300, default="")
