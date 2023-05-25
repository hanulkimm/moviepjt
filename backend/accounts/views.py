from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from .serializers import UserSerializer, UserNicknameSerializer
from django.conf import settings
User = get_user_model()

# Create your views here.
@api_view(['POST'])
def upload_profile(request, username):
    user = get_object_or_404(User, username = username)
    if request.FILES.get('profile_url'):
        uploaded_file = request.FILES['profile_url']
        user.profile = uploaded_file
        user.save()
        default_storage.save(uploaded_file.name, uploaded_file)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_profile(request, username):
    user = get_object_or_404(User,username = username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def save_nickname(request, username):
    user = get_object_or_404(User, username = username)
    if request.data.get('nickname') :
        print('change password')
        user.nickname = request.data.get('nickname')
        user.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_nickname(request, username):
    user = get_object_or_404(User,username = username)
    serializer = UserNicknameSerializer(user)
    return Response(serializer.data)