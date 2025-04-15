from .models import Genre, Video
from .serializers import GenreWithVideosSerializer, DetailVideoSerializer, VideoSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT) 


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class ListUnwatchedVideos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        genres = Genre.objects.all()
        data = []
        for genre in genres:
            unwatched_videos = genre.videos.filter(video_progress=0.0)
            if unwatched_videos.exists():
                serializer = VideoSerializer(unwatched_videos, many=True)
                data.append({"genre_name": genre.genre_name, "videos": serializer.data})
        return Response(data=data, status=status.HTTP_200_OK)


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class ListWatchedVideos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        videos = Video.objects.filter(video_progress__gt=0.0, video_progress__lt=F("video_duration"))
        data = []
        serializer = VideoSerializer(videos, many=True)
        data.append({"genre_name": "keep watching", "videos": serializer.data})
        return Response(data=data, status=status.HTTP_200_OK)
    

@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class VideoDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id):
        video = Video.objects.get(id=id)
        serializer = DetailVideoSerializer(video)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request, id):
        video = Video.objects.get(id=id)
        serializer = DetailVideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  