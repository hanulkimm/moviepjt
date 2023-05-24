from rest_framework.response import Response
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers.movie_location import LocationSerializer,MovieSerializer
from .serializers.movie_comment import CommentSerializer
from .serializers.movie_detail import MovieLocationDetailSerializer,LocationDetailSerializer
from .models import Movies, Comment, Location, LocationDetail

from django.db.models import Prefetch
# Create your views here.
 

@api_view(['POST'])   
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def comment_list(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    comments = Comment.objects.filter(movie=movie)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
def comment_edit(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method=='DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method=='PUT':
        if request.user == comment.user:
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
    


# 행정구역& 시군구에 따른 영화 리스트 출력    
@api_view(['GET'])
def location_movies(request, state, city):
    location = get_object_or_404(Location, state=state, city=city)
    serializer = LocationSerializer(location)
    return Response(serializer.data)

# 행정구역에 따른 영화 리스트 출력
@api_view(['GET'])
def state_location_movies(request, state):
    locations = Location.objects.filter(state=state).prefetch_related(
        Prefetch('movies', queryset=Movies.objects.distinct(), to_attr='unique_movies')
    )
    distinct_movies = set()
    for location in locations:
        distinct_movies.update(location.unique_movies)
    # response_data = {
    #     'state': state,
    #     'movies': list(distinct_movies)
    # }
    # return Response(response_data)
    serializer = MovieSerializer(distinct_movies, many=True)
    # location = get_list_or_404(Location, state=state)
    # serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

# 특정 영화 detail 
@api_view(['GET'])
def movie_detail(request, movie_pk, state):
    movie = Movies.objects.get(pk=movie_pk)
    location_details = LocationDetail.objects.filter(movie=movie, location__state=state)
    serializer = MovieLocationDetailSerializer(movie)
    data = serializer.data
    data['location_details'] = LocationDetailSerializer(location_details, many=True).data

    return Response(data)