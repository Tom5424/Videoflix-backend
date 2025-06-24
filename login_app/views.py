from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import CustomUser


class GuestLoginView(APIView):


    def post(self, request):
        guestUser, created = CustomUser.objects.get_or_create(username='guest', defaults={"email": "guest@guest.com"})
        token, created = Token.objects.get_or_create(user=guestUser)
        return Response({"key": token.key })