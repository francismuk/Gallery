from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    categories = Category.get_all_categories()
    locations = Location.get_all_locations()
    return render(request,'index.html', {'title':title,'images':images, 'categories':categories, 'locations':locations})

def single_image(request, category_name, image_id):
    locations = Location.objects.all()
    image = Image.get_image_by_id(image_id)
    images = Image.objects.filter(category__photo_category = category_name)
    title = f'{category_name}'
    return render(request,'single_image.html',{'title':title, 'image':image, 'images':images, 'locations':locations})

def location_filter(request, location):
    locations = Location.objects.all()
    images = Image.filter_by_location(location)
    title = f'{location} Photos'
    return render(request, 'locations.html', {'title':title, 'images':images, 'locations':locations})

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images_found = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'images':images_found, 'locations':locations})
    else:
        message = "Please enter a search object"
        return render(request, 'search.html',{'message':message})