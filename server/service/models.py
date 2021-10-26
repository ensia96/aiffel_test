from django.db import models
from server.models import BaseModel
from user.models import User


class Post(BaseModel):
    title = models.CharField(max_length=150, verbose_name="제목")
    content = models.TextField(max_length=30000, verbose_name="본문")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자")

    class Meta:
        db_table = "post"
        verbose_name = "게시글"
        app_label = "service"


class Comment(BaseModel):
    content = models.TextField(max_length=30000, verbose_name="내용")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name="게시글")

    class Meta:
        db_table = "comment"
        verbose_name = "댓글"
        app_label = "service"


class LikeForPost(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="사용자")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name="게시글")

    class Meta:
        db_table = "like_for_post"
        verbose_name = "좋아요(게시글)"
        app_label = "service"


class LikeForComment(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="사용자")
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, verbose_name="댓글")

    class Meta:
        db_table = "like_for_comment"
        verbose_name = "좋아요(댓글)"
        app_label = "service"
