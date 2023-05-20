from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:location_pk>/', views.location_movies),
    path('movies/<int:movie_pk/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),
    # path('movies/<int:article_pk>/', views.movie_detail),
]