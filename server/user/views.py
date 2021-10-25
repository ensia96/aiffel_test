import json

from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
from django.http import JsonResponse as res

from .models import User


def signup(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    data = json.loads(req.body)

    try:
        User.objects.create(
            username=data["username"],
            password=make_password(data["password"]),
            nickname=data["nickname"],
            email=data["email"],
            age=data["age"],
            phone=data["phone"],
        )

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    except IntegrityError as E:
        return res({"message": str(E).split(".").pop() + " aleady exists."}, status=400)

    return res({"message": "user data is "}, status=201)
