from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('details/<int:movie_id>', views.details, name='details'),
]