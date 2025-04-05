from django.db import models

import photo


# Create your models here.

class Userprofile(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='imgs/%Y/%m/%d',verbose_name="photo")

    class Meta:
        db_table = 'photo'
        verbose_name = '图片'
        verbose_name_plural = verbose_name