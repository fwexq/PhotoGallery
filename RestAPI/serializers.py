from rest_framework import serializers

from compet.settings import API_SCHEME, API_DOMAIN, API_PORT, MEDIA_ROOT_SHORT
from main.models import *


class UserSerializers(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email", "avatar_url")

    @classmethod
    def get_avatar_url(cls, record):
        if record.avatar:
            return f'{API_SCHEME}://{API_DOMAIN}:{API_PORT}/{MEDIA_ROOT_SHORT}/{record.avatar}'


class PostSerializers(serializers.ModelSerializer):
    author = UserSerializers(read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "title", "description", "author", "photo_url")

    @classmethod
    def get_photo_url(cls, record):
        if record.photo:
            return f'{API_SCHEME}://{API_DOMAIN}:{API_PORT}/{MEDIA_ROOT_SHORT}/{record.photo}'


class CommentSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    post = PostSerializers()

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "text", "created_at", "updated_at", "parent")
