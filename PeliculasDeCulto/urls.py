from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.dizilerdetay, name = "movie_details"),
    path('commends', views.commends),
    #path('stars',views.starsmovie),
    path('category/<int:category_id>', views.getMoviesByCategoryId),
    path('category/<str:category_name>', views.getMoviesByCategory, name = 'movies_by_category'),
]
