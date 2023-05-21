from django.urls import path
from . import views

urlpatterns = [
    path('movies/location/<int:location_pk>/', views.location_movies),
    path('movies/detail/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_edit),

]