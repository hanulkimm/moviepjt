from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_pk>/<str:profile_url>/', views.upload_profile)
]
