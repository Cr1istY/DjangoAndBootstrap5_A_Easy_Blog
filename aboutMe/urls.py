from django.urls import path
from . import views

app_name = 'aboutMe'

urlpatterns = [
    path('', views.about, name='Me'),
    path('aboutMe/', views.about_me, name='aboutMe'),

]