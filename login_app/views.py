from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import CustomUser


class GuestLoginView(APIView):


    def post(self, request):
        try:
            customUser = CustomUser.objects.get(username='guest')
        except CustomUser.DoesNotExist:
            return Response({"error": "Guest account not found."}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=customUser)
        return Response({"key": token.key })