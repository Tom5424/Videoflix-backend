from .models import Genre
from .serializers import GenreWithVideosSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT) 


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class ListVideos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreWithVideosSerializer(genre, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)