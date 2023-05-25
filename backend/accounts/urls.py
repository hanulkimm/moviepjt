from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.upload_profile),
    path('getprofile/<str:username>/', views.get_profile)
] 