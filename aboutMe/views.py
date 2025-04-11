from django.shortcuts import render
from .models import Wisdom
import random
# Create your views here.

def about(request):
    wisdoms = Wisdom.objects.all()
    random_wisdom = random.choice(wisdoms)
    return render(request, 'Me/personalWeb/webs/index.html', context={'wisdom': random_wisdom})

def about_me(request):
    return render(request, 'Me/personalWeb/webs/aboutMe.html')