from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from .room import Room

class Item(models.Model):
     name = models.CharField(max_length=50)
     location = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
     image = models.CharField(max_length=200)
     price = models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(200000.00)],)
