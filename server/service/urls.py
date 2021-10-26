from django.urls import path
from . import views

urlpatterns = [
    path("post/create/", views.create_post, name="create-post"),
]
