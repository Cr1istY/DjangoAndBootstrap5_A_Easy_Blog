from django.shortcuts import render
from .models import Userprofile
import random

# Create your views here.
def photo_view(request):
    icons = Userprofile.objects.all()
    return render(request, 'photo/photo.html', context={'icons':icons})