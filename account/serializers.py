from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id','email','username','phone','image','isAdmin','first_name','last_name']

    def get_isAdmin(self,obj):
        return obj.is_staff

    def get_username(self,obj):
        return obj.username


class UserWithTokenSerializer(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','email','username','isAdmin','token']
    
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


