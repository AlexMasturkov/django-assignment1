from django.db import models

# Create your models here.

class Snake(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    color_pattern = models.CharField(max_length=128)
    favourite_prey = models.CharField(max_length=128)
    region = models.CharField(max_length=64)
    venomous = models.BooleanField(default=True)

