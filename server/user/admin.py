from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("nickname", "email", "created_at")
    list_display_links = ("nickname", "email")
