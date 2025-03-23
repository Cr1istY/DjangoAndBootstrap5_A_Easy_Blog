from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('blog/detail/<blog_id>', views.blog, name='blog_detail'),
    path('blog/pub', views.pub, name='blog_publish'),
    path('blog/comment/pub', views.pub_comment, name='pub_comment'),
    path('search', views.search, name='search'),
]