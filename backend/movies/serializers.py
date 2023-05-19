from rest_framework import serializers
from .models import Movies, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)

# class MovieSerializer(serializers.ModelSerializer):
