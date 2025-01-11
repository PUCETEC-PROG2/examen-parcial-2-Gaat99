from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index.html"), 
    path("<int:movie_id>/", views.movie_details, name="movie_detail"),  
    path("add/", views.add_movie, name="add_movie"), 
]