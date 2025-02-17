from dj_rest_auth.serializers import PasswordResetConfirmSerializer
from rest_framework import serializers


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):


    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except serializers.ValidationError:
            raise serializers.ValidationError({'token': "The password reset link is invalid or expired. Please request a new link."})
        return data