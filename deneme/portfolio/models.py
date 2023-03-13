from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# Create your models here.
