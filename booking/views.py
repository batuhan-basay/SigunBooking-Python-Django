from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Places,Place_Img, Categories, Places_Features

# Create your views here.

def index(request):
    context = {
        "places": Places.objects.filter(is_active = True, is_home=True),
        "categories":Categories.objects.all()
    }
    return render(request, "home/index.html",context)

def places(request):
    context = {
        "places": Places.objects.filter(is_active = True, is_home=True),
        "categories":Categories.objects.all()
    }
    return render(request, "places/index.html", context)

def places_details(request,slug):
    places = Places.objects.get(slug=slug)
    context = {
        "places": Places.objects.get(slug=slug),
        "place_img": Place_Img.objects.filter(Places=places.id),
        "place_features":Places_Features.objects.filter(Places=places.id)
    }
  

    return render(request, "places/places_details.html",context)

def blogs(request):
    return render(request, "blogs/index.html")

def blog_details(request, id):
    return render(request, "blogs/blog_details.html", {"id":id})
