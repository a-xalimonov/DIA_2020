from django.shortcuts import render
from .models import movie, detail

# Create your views here.
def movies(request):
    films = movie.objects.all()
    return render(request,'movies/movies.html', {'films':films})
    
def details(request, movie_id):
    movie_link = movie.objects.get(id = movie_id)
    details = detail.objects.filter(movie_link = movie_id)
    return render(request,'movies/details.html', {'movie_link':movie_link, 'details':details})