from rest_framework import serializers
from movies.models import Movies, Comment, Location, LocationDetail,Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        # fields ='__all__'
        exclude = ['id',]

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movies
        fields = ['id','genres','release_date','director_name','movie_title','nation','plot','runtime','rating','keywords','poster']

class LocationSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Location
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        movies = representation['movies']
        unique_movies = []
        seen_movie_ids = set()
        
        for movie in movies:
            movie_id = movie['id']
            if movie_id not in seen_movie_ids:
                unique_movies.append(movie)
                seen_movie_ids.add(movie_id)
        
        representation['movies'] = unique_movies
        return representation


