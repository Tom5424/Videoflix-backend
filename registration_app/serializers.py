from login_app.models import CustomUser
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer 


class CustomRegistrationSerializer(RegisterSerializer):
    username = None


    def validate_email(self, email):
        email = super().validate_email(email)
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email