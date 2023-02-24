from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "home/index.html")

def blogs(request):
    return render(request, "blogs/index.html")

def blog_details(request, id):
    return render(request, "blogs/blog_details.html", {"id":id})
