from django.db import models
from server.models import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=50, unique=True, verbose_name="아이디")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    nickname = models.CharField(max_length=50, verbose_name="닉네임")
    email = models.EmailField(max_length=80, unique=True, verbose_name="이메일")
    age = models.IntegerField(blank=True, verbose_name="나이")
    phone = models.CharField(blank=True, max_length=13, verbose_name="핸드폰 번호")

    class Meta:
        db_table = "user"
        verbose_name = "유저"
        app_label = "user"
