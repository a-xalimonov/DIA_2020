from django.urls import path
from . import views

urlpatterns = [
    path('', views.comics, name='comics'),
    path('read/<int:comic_id>/', views.read, name='read'),
]