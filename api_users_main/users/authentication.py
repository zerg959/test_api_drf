import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from .models import CustomUser


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token = auth_data.decode("utf-8").split(" ")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload["user_id"]
            user = CustomUser.objects.get(id=user_id)
            return (user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Your token is invalid,login")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Your token is expired,login")

        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
