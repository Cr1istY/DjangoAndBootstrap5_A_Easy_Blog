from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-pub_date']



class BlogComment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog,related_name='comments' ,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-pub_date']
