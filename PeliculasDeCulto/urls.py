from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.dizilerdetay, name = "movie_details"),
    path('category/<slug:slug>', views.getMoviesByCategory, name = 'movies_by_category'),
    #path('commends', views.commends),
    #path('stars',views.starsmovie),
]
   
