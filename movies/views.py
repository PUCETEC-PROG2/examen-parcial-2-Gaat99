from django.http import HttpResponse
from django.template import loader
from .models import Movie
from movies.forms import MovieForm
from django.shortcuts import redirect, render 
from django.contrib.auth.views import LoginView


def index(request):
    moviesxd = Movie.objects.all()  
    return render(request, '/index.html', {'movies': moviesxd})
    
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')  
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})



def movie_details(request, movies_id): 
    movies = movies.objects.get(id = movies_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))
