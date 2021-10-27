from django.urls import path
from . import views

urlpatterns = [
    path("post/create/", views.create_post, name="create-post"),
    path("posts/", views.get_post_list, name="get-post-list"),
    path("post/search/", views.search_post, name="search-post"),
    path("post/top/", views.get_top_post, name="get-top-post"),
    path("post/<int:post_id>", views.get_post, name="get-post"),
    path("post/update/", views.update_post, name="update-post"),
    path("post/delete/<int:post_id>", views.delete_post, name="delete-post"),
    path("post/like/<int:post_id>", views.like_post, name="like-post"),
    path("comment/add/", views.add_comment, name="add-comment"),
    path("comments/<int:post_id>", views.get_comment_list, name="get-comment-list"),
]
