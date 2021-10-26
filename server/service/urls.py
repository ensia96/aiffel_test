from django.urls import path
from . import views

urlpatterns = [
    path("post/create/", views.create_post, name="create-post"),
    path("posts/", views.get_post_list, name="get-post-list"),
    path("post/search/", views.search_post, name="search-post"),
    path("post/<int:post_id>/", views.get_post, name="get-post"),
    path("post/update/", views.update_post, name="update-post"),
    path("post/delete/<int:post_id>/", views.delete_post, name="delete-post"),
]
