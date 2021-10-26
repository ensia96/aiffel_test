import json

from django.db.models import Count, F
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


def get_post_list(req):
    if req.method != "GET":
        return res({"message": "this method is not allowed."}, status=400)

    posts = Post.objects.values(
        'title',
        'created_at'
    ).annotate(
        author_id=F('user__id'),
        author_nickname=F('user__nickname'),
        likes=Count('likeforpost')
    )

    return res({"posts": list(posts)}, status=200)
