from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('profile/<int:user_pk>/', views.upload_profile),
    path('getprofile/<int:user_pk>/', views.get_profile)
] + static(settings.MEDIA_URL, docuument_root=settings.MEDIA_ROOT)
