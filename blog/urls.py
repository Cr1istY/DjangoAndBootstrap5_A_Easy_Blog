from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('detail/<blog_id>', views.blog, name='blog_detail'),
    path('pub', views.pub, name='blog_publish'),
    path('comment/pub', views.pub_comment, name='pub_comment'),
    path('search', views.search, name='search'),
    path('recommend', views.recommend, name='recommend'),
]