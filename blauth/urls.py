from django.urls import path
from . import views

app_name = 'blauth'

urlpatterns = [
    path('login/', views.bllogin, name='bllogin'),
    path('logout/', views.blog_logout, name='bllogout'),
    path('register/', views.register, name='register'),
    path('register/captcha/', views.send_email_captcha, name='email'),

]