from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
from darkflow.helper import Response


class CustomUser(AbstractUser):
    image = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)
    email_active = models.BooleanField(default=False)

    @staticmethod
    def update_user(request, serializer):
        user = CustomUser.objects.get(pk=request.user.pk)
        user_srz = serializer(instance=user, data=request.data, partial=True)
        if user_srz.is_valid():
            user_srz.save()
            res = Response(user_srz.data, status.HTTP_200_OK)
            return res
        res = Response(user_srz.errors, status.HTTP_400_BAD_REQUEST)
        return res

    @staticmethod
    def create_user(request, serializer):
        try:
            data = request.data
            user = CustomUser.objects.create(
                username = data['username'],
                email = data['email'],
                password = make_password(data['password'])
            ) 
            serializer = serializer(user,many=False)
            res = Response(serializer.data, status.HTTP_200_OK)
            return res

        except Exception as e:
            res = Response(str(e), status.HTTP_400_BAD_REQUEST)
            return res

    def __str__(self):
        return self.username

