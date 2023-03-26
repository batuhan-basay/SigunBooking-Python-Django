
from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Places,Place_Img, Categories,Cities, Places_Features
from django.views.generic import TemplateView, ListView

# Create your views here.

def index(request):
    context = {
        "places": Places.objects.filter(is_active = True, is_home=True),
        "categories":Categories.objects.all(),
        "cities":Cities.objects.all()
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

def search(request):
    _search = request.GET.get('search')
    _category = request.GET.get('category')
    _city = request.GET.get('city')

    if _category is not None and _search != "" and _city is not None:
        print("ikiside")
        context = {
            "places":  Places.objects.filter(category__category_name__icontains=_category) | Places.objects.filter(title__icontains=_search),
            "categories":Categories.objects.all(),
            "cities":Cities.objects.all()
        }
    elif _category is not None:
        print("category")
        context = {
            "places":  Places.objects.filter(category__category_name__icontains=_category),
            "categories":Categories.objects.all(),
            "cities":Cities.objects.all()
        }
    elif _city is not None:
        print("city")
        context = {
            "places": Places.objects.filter(cities__city__icontains=_city),
            "categories":Categories.objects.all(),
            "cities":Cities.objects.all()
        }
    elif _search != "":
        print("search")
        context = {
            "places": Places.objects.filter(title__icontains=_search),
            "categories":Categories.objects.all(),
            "cities":Cities.objects.all()
        }
    elif _category is None or _search == "" :
        context = {
            "categories":Categories.objects.all(),
            "cities":Cities.objects.all()
        }

    return render(request, "places/index.html",context)


def blogs(request):
    return render(request, "blogs/index.html")

def blog_details(request, id):
    return render(request, "blogs/blog_details.html", {"id":id})
