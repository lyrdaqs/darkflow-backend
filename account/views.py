from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserWithTokenSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .tasks import send_email
from django.contrib.auth.tokens import default_token_generator
import requests
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserWithTokenSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegister(APIView):
     def post(self, request):
        res = CustomUser.create_user(request, UserWithTokenSerializer)
        return Response(res.result, res.status)


class EditProfile(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        res = CustomUser.update_user(request, UserSerializer)
        return Response(res.result, res.status)


class VertifyEmail(APIView):
    permission_classes = [IsAuthenticated]
    activate_link_url = "http://127.0.0.1:8000/account/active_user"

    def get(self, request):
        confirmation_token = default_token_generator.make_token(request.user)
        send_email.delay(
            "vertify your email for Darkflow",
            f"your activate link:{self.activate_link_url}?user_id={request.user.id}&confirmation_token={confirmation_token}",
            "lyrdaq777@gmail.com",
            [request.user.email]
        )
        return Response({'message':"your activation link sended to your email"})


class ActiveUserWithEmail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.query_params.get('user_id', '')
        confirmation_token = request.query_params.get('confirmation_token', '')
        exist_user = CustomUser.objects.get(pk=user_id)
        if exist_user == None:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(exist_user, confirmation_token):
            return Response('Token is invalid or expired. Please request another confirmation email by signing in.',
                         status=status.HTTP_400_BAD_REQUEST)
        exist_user.email_active = True
        exist_user.save()
        return Response('Email successfully confirmed')


class PasswordResteRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        confirmation_token = request.query_params.get('token', '')
        data = {
            "token": confirmation_token
        }
        res = requests.post(f'{settings.DOMAIN_NAME}/account/password_reset/validate_token/', data)
        return Response(res.json())


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response(status.HTTP_204_NO_CONTENT)
