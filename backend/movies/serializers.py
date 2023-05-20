from rest_framework import serializers
from .models import Movies, Comment, Location

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id','release_date','director_name','movie_title','nation','plot','runtime','rating','keywords','poster']

class LocationMovieSerializer(serializers.ModelSerializer):
    movies = MovieDetailSerializer(many=True)
    
    class Meta:
        model = Location
        fields = ['state','city','movies',]