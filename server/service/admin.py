from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "like", "created_at")
    list_display_links = ("title",)

    def author(self, obj):
        return obj.user.nickname

    def like(self, obj):
        return len(obj.likeforpost_set.all())

    author.admin_order_field = 'user'
    author.short_description = '작성자'
    like.short_description = '좋아요'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "like", "created_at")
    list_display_links = ("content",)

    def author(self, obj):
        return obj.user.nickname

    def like(self, obj):
        return len(obj.likeforcomment_set.all())

    author.admin_order_field = 'user'
    author.short_description = '작성자'
    like.short_description = '좋아요'
