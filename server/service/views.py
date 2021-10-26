import json

from django.http import JsonResponse as res

from .models import Post
from user.models import User

from user.auth import check_token


@check_token
def create_post(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    data = json.loads(req.body)

    try:
        Post.objects.create(
            title=data['title'],
            content=data['content'],
            user=req.user
        )

    except Exception as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    return res({"message": "post creation success"}, status=201)
