from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Room(models.Model):
  name = models.CharField(max_length=20)
  user = models.ForeignKey("PieceUser", on_delete=CASCADE)
