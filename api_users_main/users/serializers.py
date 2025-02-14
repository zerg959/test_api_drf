from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.timezone import now
from django.conf import settings
import jwt
import uuid
from datetime import timedelta
from constance import config
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'refresh_token')
        read_only_fields = ('id', 'refresh_token')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(

            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            # Generate tokens
            access_token_payload = {
                "user_id": user.id,
                "expire": (
                    now() + timedelta(days=config.JWT_ACCESS_TOKEN_LIFETIME_DAYS)
                ).isoformat(),
                "issued": now().isoformat(),
            }
            access_token = jwt.encode(
                access_token_payload, settings.SECRET_KEY, algorithm="HS256"
            )
            refresh_token = uuid.uuid4()
            user.refresh_token = refresh_token
            user.save()
            return {"access_token": access_token, "refresh_token": str(refresh_token)}
        raise serializers.ValidationError("Wrong username/password data")


class TokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        refresh_token = data.get("refresh_token")
        try:
            user = CustomUser.objects.get(refresh_token=refresh_token)
            if not user.refresh_token or (now() - user.date_joined) > timedelta(
                days=config.JWT_REFRESH_TOKEN_LIFETIME_DAYS
            ):
                # If refresh token истек generate new pair of tokens
                access_token_payload = {
                    "user_id": user.id,
                    "expire": (
                        now() + timedelta(days=config.JWT_ACCESS_TOKEN_LIFETIME_DAYS)
                    ).isoformat(),
                    "issued": now().isoformat(),
                }
                access_token = jwt.encode(
                    access_token_payload, settings.SECRET_KEY, algorithm="HS256"
                )
                new_refresh_token = uuid.uuid4()
                user.refresh_token = new_refresh_token
                user.save()
                return {
                    "access_token": access_token,
                    "refresh_token": str(new_refresh_token),
                }
            else:
                # If refresh token valid, refresh access token
                access_token_payload = {
                    "user_id": user.id,
                    "expire": (
                        now() + timedelta(days=config.JWT_ACCESS_TOKEN_LIFETIME_DAYS)
                    ).isoformat(),
                    "issued": now().isoformat(),
                }
                access_token = jwt.encode(
                    access_token_payload, settings.SECRET_KEY, algorithm="HS256"
                )
                return {
                    "access_token": access_token,
                    "refresh_token": str(user.refresh_token),
                }
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid refresh token")
