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

class LocationDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = LocationDetail
        # fields = '__all__'
        exclude = ['id',]

class LocationSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()

    class Meta:
        model = Location
        # fields = '__all__'
        exclude = ['movies',]

    
    def get_location_details(self, obj):
        location_details = obj.locationdetail_set.all()
        serializer = LocationDetailSerializer(location_details,many=True)
        return serializer.data