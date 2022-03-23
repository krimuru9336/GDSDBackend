from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
import logging
from django.contrib.auth.models import User


@database_sync_to_async
def get_user(user_jwt):
    try:

        return User.objects.get(id=user_jwt)
    except User.DoesNotExist:

        return AnonymousUser()


class TokenAuthMiddleware:
    """
    Custom token auth middleware
    """


    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner


    def __call__(self, scope):




        # Get the token
        token =parse_qs(scope["query_string"].decode("utf8"))["token"][0]

        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            return None
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])


            # Will return a dictionary like -
            # {
            #     "token_type": "access",
            #     "exp": 1568770772,
            #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
            #     "user_id": 6
            # }

            # Get the user using ID

            #user = User.objects.get(id=decoded_data["user_id"])
            user = decoded_data['user_id']
            #user = 'syednaqi53@gmail.com'

        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user))

