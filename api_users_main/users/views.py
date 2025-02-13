from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import (RegisterSerializer, LoginSerializer,
                          TokenRefreshSerializer, UserSerializer)

class RegisterView(APIView):
    permission_classes = [AllowAny,]  # Allow all to register.

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data,
                            status=status.HTTP_201_CREATED
                            )
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                        )

class LoginView(APIView):
    permission_classes = [AllowAny,] 

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,
                            status=status.HTTP_200_OK
                            )
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                        )

class TokenRefreshView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = TokenRefreshSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,
                            status=status.HTTP_200_OK
                            )
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                        )
