from rest_framework import serializers
from movies.models import Movies, Genre, Actor

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id',]

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name','actorProfile_path']

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movies
        fields = ['genres','actors','release_date','director_name','movie_title','nation','plot','runtime','rating','keywords','poster']