from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
# Create your models here.

class CaptchaModel(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=4)
    creat_time = models.DateTimeField(auto_now_add=True)

