from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    return render(request,'index.html', {'title':title,'images':images})

