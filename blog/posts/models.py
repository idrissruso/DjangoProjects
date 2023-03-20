from django.db import models
from django.utils import timezone

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=10000,default="hello wordl")
    time = models.DateTimeField(default=timezone.now)