from rest_framework.response import Response
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers.movie_location import LocationSerializer
from .serializers.movie_comment import CommentSerializer
from .serializers.movie_detail import MovieDetailSerializer
from .models import Movies, Comment, Location
# Create your views here.
 

@api_view(['POST'])   
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['DELETE', 'PUT'])
def comment_edit(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_likes(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    


# 행정구역에 따른 영화 리스트 출력    
@api_view(['GET'])
def location_movies(request, state, city):
    location = get_list_or_404(Location, state=state, city=city)
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)

# 특정 영화 detail 
@api_view(['GET'])
def movie_detail(request, movie_pk):
    print(1)
    movie = get_object_or_404(Movies, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)