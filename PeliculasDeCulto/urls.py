from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search',views.search, name="search"),
    path('create-movie',views.create_movie, name="create_movie"),
    path('movie-list', views.movie_list, name="movie_list"),
    path('movie-edit/<int:id>', views.movie_edit, name="movie_edit"),
    path('<slug:slug>', views.dizilerdetay, name="movie_details"),
    path('category/<slug:slug>', views.getMoviesByCategory, name = 'movies_by_category'),
    #path('commends', views.commends),
    #path('stars',views.starsmovie),
]
   
