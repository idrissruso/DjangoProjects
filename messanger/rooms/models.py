from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    
class Message(models.Model):
    content = models.CharField(max_length=10000)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=False
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        blank=False
        )
    
    
