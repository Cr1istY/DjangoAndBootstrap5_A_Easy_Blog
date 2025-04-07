from django.shortcuts import render
from .models import Userprofile


# Create your views here.
def photo_view(request):
    imgs = Userprofile.objects.all()
    return render(request, 'photo/photo.html', context={'imgs':imgs})