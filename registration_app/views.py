from dj_rest_auth.registration.views import VerifyEmailView
from allauth.account.models import EmailConfirmation 
from rest_framework.response import Response
from rest_framework import status


class CustomVerifyEmailView(VerifyEmailView):


    def post(self, request, *args, **kwargs):
        key = request.data.get("key")
        email_confirmation = EmailConfirmation.objects.get(key=key)
        if email_confirmation.email_address.verified:
            return Response(data={"detail": "Email is already verified."}, status=status.HTTP_200_OK)
        super().post(request, *args, **kwargs)
        return Response(data={"detail": "Email successfully verified."}, status=status.HTTP_200_OK)