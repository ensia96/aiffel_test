import json

from django.db.models import Count, F, Q
from django.http import JsonResponse as res
from django.core.exceptions import FieldError

from .models import Post, LikeForPost, Comment
from user.models import User

from user.auth import check_token


@check_token
def create_post(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        data = json.loads(req.body)

        Post.objects.create(
            title=data["title"],
            content=data["content"],
            user=req.user
        )

    except json.decoder.JSONDecodeError:
        return res({"message": "there is problem with the request body."}, status=400)

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    return res({"message": "successfully created post."}, status=201)


def get_post_list(req):
    if req.method != "GET":
        return res({"message": "this method is not allowed."}, status=400)

    posts = Post.objects.values(
        "id",
        "title",
        "created_at"
    ).annotate(
        author_id=F("user__id"),
        author_nickname=F("user__nickname"),
        likes=Count("likeforpost", distinct=True),
        comments=Count("comment", distinct=True)
    )

    return res({"posts": list(posts)}, status=200)


def search_post(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        data = json.loads(req.body)
        query = Q()

        search_type = data["type"]+"__icontains"
        search_keywords = data["keyword"].split()

        for search_keyword in search_keywords:
            detail = {search_type: search_keyword}
            query.add(Q(**detail), Q.OR)

        posts = Post.objects.values(
            "id",
            "title",
            "created_at"
        ).annotate(
            author_id=F("user__id"),
            author_nickname=F("user__nickname"),
            likes=Count("likeforpost", distinct=True),
            comments=Count("comment", distinct=True)
        ).filter(query)

    except json.decoder.JSONDecodeError:
        return res({"message": "there is problem with the request body."}, status=400)

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    except FieldError:
        return res({"message": "this search type is not supported."}, status=400)

    return res({"posts": list(posts)}, status=200)


def get_post(req, post_id):
    if req.method != "GET":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        post = Post.objects.values(
            "id",
            "title",
            "content",
            "created_at",
            "updated_at"
        ).annotate(
            author_id=F("user__id"),
            author_nickname=F("user__nickname"),
            likes=Count("likeforpost")
        ).get(id=post_id)

    except Post.DoesNotExist:
        return res({"message": "post does not exist."}, status=404)

    return res({"post": post}, status=200)


@check_token
def update_post(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        data = json.loads(req.body)
        post = Post.objects.get(id=data["id"], user=req.user)

        post.title = data["title"]
        post.content = data["content"]

        post.save()

    except json.decoder.JSONDecodeError:
        return res({"message": "there is problem with the request body."}, status=400)

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    except Post.DoesNotExist:
        return res({"message": "this user can not update this post."}, status=403)

    return res({"message": "successfully updated post."}, status=200)


@check_token
def like_post(req, post_id):
    if req.method != "PUT":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        post = Post.objects.get(id=post_id)
        liked = LikeForPost.objects.filter(post=post, user=req.user)
        already_liked = liked.exists()

        if already_liked:
            liked[0].delete()
        else:
            LikeForPost.objects.create(post=post, user=req.user)

    except Post.DoesNotExist:
        return res({"message": "post does not exist."}, status=404)

    return res({"message": ["", "un"][already_liked]+"liked the post."}, status=200)


@check_token
def delete_post(req, post_id):
    if req.method != "DELETE":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        post = Post.objects.get(id=post_id, user=req.user)
        post.delete()

    except Post.DoesNotExist:
        return res({"message": "this user can not delete this post."}, status=403)

    return res({"message": "successfully deleted post."}, status=200)


@check_token
def add_comment(req):
    if req.method != "POST":
        return res({"message": "this method is not allowed."}, status=400)

    try:
        data = json.loads(req.body)
        post = Post.objects.get(id=data["post_id"])

        Comment.objects.create(
            content=data["content"],
            post=post,
            user=req.user
        )

    except json.decoder.JSONDecodeError:
        return res({"message": "there is problem with the request body."}, status=400)

    except KeyError as E:
        return res({"message": str(E) + " is not provided."}, status=400)

    except Post.DoesNotExist:
        return res({"message": "post does not exist."}, status=404)

    return res({"message": "successfully added comment."}, status=201)
