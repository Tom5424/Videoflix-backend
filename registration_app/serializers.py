from dj_rest_auth.registration.serializers import RegisterSerializer 


class CustomRegistrationSerializer(RegisterSerializer):
    username = None