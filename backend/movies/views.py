from rest_framework.response import Response
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, CommentSerializer, LocationMovieSerializer
from .models import Movies, Comment, Location
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method=='GET':
        movies = get_list_or_404(Movies)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
# @api_view(['GET'])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movies, pk=movie_pk)
#     serializer = 

@api_view(['POST'])   
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='POST':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 행정구역에 따른 영화 리스트 출력(아직 중개 테이블 추가 못해줌)        
@api_view(['GET'])
def location_movies(request, location_pk):
    location = get_list_or_404(Location,pk=location_pk)
    if request.method=='GET':
        serializer = LocationMovieSerializer(location, many=True)
        return Response(serializer.data)
