from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# @api_view(["GET"])
# def get_videos(request):
#     return Response("asds")


class ListVideos(APIView):


    def get(self, request):
        return Response("asds")