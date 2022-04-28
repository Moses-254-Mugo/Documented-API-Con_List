from asyncio import exceptions
import jwt
from rest_framework import authentication
from django.conf import settings

class JWTAuthentication(authentication.BaseAuthentication):
    def authentication(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
        except jwt.DecodeError as identifire:
            raise exceptions.AuthenticationFailed
 

        return super().authenticate(request)

