from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(default='profile.jpg')
    nickname = models.CharField(max_length=200, default='아무개')
