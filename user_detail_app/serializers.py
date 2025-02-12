from login_app.models import CustomUser
from dj_rest_auth.serializers import UserDetailsSerializer


class CustomUserDetailSerializer(UserDetailsSerializer):


    class Meta:
        model = CustomUser 
        fields = ["id", "email", "username", "first_name", "last_name"]    


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, 'username'):
            representation['username'] = instance.username
        return representation