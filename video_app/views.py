from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 


class ListVideos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(data=serializer.data)