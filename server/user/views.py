import json

from django.contrib.auth.hashers import make_password, check_password
from django.db.utils import IntegrityError
from django.http import JsonResponse as res

from .models import User
from .auth import create_token


def signup(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        data = json.loads(req.body)

        User.objects.create(
            username=data["username"],
            password=make_password(data["password"]),
            nickname=data["nickname"],
            email=data["email"],
            age=data["age"],
            phone=data["phone"],
        )

    except json.decoder.JSONDecodeError:
        return res({"message": "there is problem with the request body."}, status=400)

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    except IntegrityError as E:
        return res({"message": str(E).split(".").pop() + " aleady exists."}, status=400)

    return res({"message": "signup success."}, status=201)


def signin(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        data = json.loads(req.body)

        user = User.objects.get(username=data["username"])
        valid = check_password(data["password"], user.password)
        if not valid:
            raise Exception
        token = create_token(user)

    except json.decoder.JSONDecodeError:
        return res({"message": "there is problem with the request body."}, status=400)

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    except Exception as E:
        return res({"message": "user data is not valid."}, status=400)

    return res({"message": "singin success.", "token": token}, status=200)
