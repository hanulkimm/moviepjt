from rest_framework import serializers
from movies.models import Movies, Genre, Actor,Comment, Location, LocationDetail

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id',]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name','profile_path']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDetail
        fields = ('place',)


class MovieLocationDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    location_details = LocationDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Movies
        # exclude = ['kmdb_id','tmdb_id','kmdb_seq']
        fields = ['genres','actors','comment_set','release_date','director_name','movie_title','nation','plot','runtime','rating','keywords','poster','location_details']

