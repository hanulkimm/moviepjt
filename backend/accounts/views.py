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
from .serializers import UserSerializer
from django.conf import settings
User = get_user_model()

# Create your views here.
@api_view(['POST'])
def upload_profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.FILES.get('profile_url'):
        uploaded_file = request.FILES['profile_url']
        user.profile = uploaded_file
        user.save()
        default_storage.save(uploaded_file.name, uploaded_file)
        # file_url = default_storage.url(file_name)
        # user.profile = file_url
        # user.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    # profile_url = serializer.data['profile']
    # full_profile_url = request.build_absolute_uri(settings.MEDIA_URL + profile_url)
    # serializer.data['profile'] = full_profile_url
    return Response(serializer.data)