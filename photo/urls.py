from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('view',views.photo_view, name='photo_view'),

]