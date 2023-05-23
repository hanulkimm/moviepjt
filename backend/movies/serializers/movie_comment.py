from rest_framework import serializers
from movies.models import Movies, Comment, Location, LocationDetail,Genre
from django.contrib.auth import get_user_model
User = get_user_model()
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like_users_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie','like_users','user',)
    
    def get_like_users_count(self, instance):
        return instance.like_users.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = data['user']['username']
        return data