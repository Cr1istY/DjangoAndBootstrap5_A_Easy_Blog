from django.db import models

# Create your models here.

class Wisdom(models.Model):
    author = models.CharField(max_length=100)
    sentence = models.CharField(max_length=100)
    article = models.CharField(max_length=100)

