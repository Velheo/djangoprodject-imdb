from django.urls import path
from . import views
app_name="imdb"

urlpatterns=[
    path('', views.IndexView.as_view(), name="index"),
    path('movies/', views.MovieListView.as_view(), name="movie_list"),
    path('movie/<int:pk>/', views.movie_detail, name="movie_detail"),
    #path('movie/<int:pk>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('movies/top/', views.BestMovieListView.as_view(), name="best_movie_list"),
    path('directors/', views.DirectorListView.as_view(), name="director_list"),
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name="director_detail"),
    path('search/', views.search, name="search"),
    path('config/', views.config, name="config"),
    path('add/movie/', views.add_movie, name="add_movie"),
 #   path('add/director/', views.add_director, name="add_director"),

# http://127.0.0.1:8000/imdb/api/movies/all
    path('api/movies/all', views.MovieListAPIView.as_view(), name='movie_list_api'),
]