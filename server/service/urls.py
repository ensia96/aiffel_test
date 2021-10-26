from django.urls import path
from . import views

urlpatterns = [
    path("post/create/", views.create_post, name="create-post"),
    path("posts/", views.get_post_list, name="get-post-list"),
    path("post/<int:post_id>/", views.get_post, name="get-post"),
]
