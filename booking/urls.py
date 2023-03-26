from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("places", views.places),
    path("places/<slug:slug>", views.places_details),
    path("search/", views.search, name="search_results"),
    path("search/search", views.search, name="search_results"),
    path("blogs", views.blogs),
    path("blog/<int:id>", views.blog_details)
]
