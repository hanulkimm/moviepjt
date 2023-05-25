from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_pk>/', views.upload_profile),
    path('getprofile/<int:user_pk>/', views.get_profile)
] 