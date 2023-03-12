from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# Create your models here.
