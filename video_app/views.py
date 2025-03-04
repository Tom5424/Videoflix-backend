from .models import Genre
from .serializers import GenreWithVideosSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ListVideos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreWithVideosSerializer(genre, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
