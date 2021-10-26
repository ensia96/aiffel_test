import os
import jwt

from django.http import JsonResponse as res

from .models import User


def create_token(user):
    key = os.environ.get("SECRET_KEY")
    payload = {"user_id": user.id}
    token = jwt.encode(payload, key, "HS256")

    return token


def check_token(func):
    def inner_func(req, *args, **kwargs):
        try:
            token = req.headers.get("Authorization")
            key = os.environ.get("SECRET_KEY")

            data = jwt.decode(token, key, "HS256")
            req.user = User.objects.get(id=data.get('user_id'))

        except Exception:
            return res({'message': 'token is not valid'}, status=401)

        return func(req, *args, **kwargs)

    return inner_func
