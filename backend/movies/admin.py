from django.contrib import admin
from .models import Movies, Location, LocationDetail, Genre, Comment, Actor
# Register your models here

admin.site.register(Movies)
admin.site.register(Location)
admin.site.register(LocationDetail)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Actor)