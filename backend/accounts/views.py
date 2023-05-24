from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@api_view(['POST'])
def upload_profile(request, user_pk, profile_url):
    user = get_object_or_404(User, pk=user_pk)
    return Response(status=status.HTTP_200_OK)
    user.profile_url = profile_url
    user.save()
    return Response(status=status.HTTP_200_OK)
