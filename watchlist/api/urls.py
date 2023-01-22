from django.urls import path
from .views import movie_list, movie_detail, MovieListAV, MoviewDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name = "movie_list"),
    path('<int:pk>/', MoviewDetailAV.as_view(), name = "movie_detail"),
]