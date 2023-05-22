from django.urls import path
from . import views

urlpatterns = [
    path('movies/detail/<int:movie_pk>/', views.movie_detail),
    path('movies/<str:state>/<str:city>/', views.location_movies),
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_edit),
    path('comments/<int:comment_pk>/likes/', views.comment_likes),
]