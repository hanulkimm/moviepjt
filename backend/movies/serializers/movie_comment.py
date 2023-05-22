from rest_framework import serializers
from movies.models import Movies, Comment, Location, LocationDetail,Genre

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)

