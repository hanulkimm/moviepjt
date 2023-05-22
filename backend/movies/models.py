from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    tmdb_actor_id = models.CharField(max_length=100)
    profile_path = models.URLField(null=True)

    def __str__(self):
        return self.actor_name

class Movies(models.Model):
    kmdb_id = models.CharField(max_length=100)
    tmdb_id = models.CharField(max_length=100, null=True)
    kmdb_seq = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=200)
    director_name = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    plot = models.TextField()
    runtime = models.CharField(max_length=100)
    rating = models.TextField()
    release_date = models.CharField(max_length=100)
    keywords = models.TextField()
    poster = models.URLField()
    teaser = models.URLField()
    genres = models.ManyToManyField(Genre, related_name='movies_genre')
    actors = models.ManyToManyField(Actor, related_name='movies_actor')

    def __str__(self):
        return self.movie_title

class Location(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movies, through='LocationDetail', related_name='locations')

    def __str__(self):
        return self.state
    

class LocationDetail(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    location= models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    place = models.TextField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)


class Comment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField()
    
    def __str__(self):
        return self.title