from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate

class CreateUserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": str(RefreshToken.for_user(user).access_token),
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():  
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                return Response({
                    "token": str(RefreshToken.for_user(user).access_token)
                })
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)