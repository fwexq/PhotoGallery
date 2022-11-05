from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from compet.settings import API_SCHEME, API_DOMAIN, API_PORT, MEDIA_ROOT_SHORT
from main.models import *


class UserSerializers(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "is_staff", "first_name", "last_name", "email", "avatar_url", "token")

    @classmethod
    def get_avatar_url(cls, record):
        if record.avatar:
            return f'{API_SCHEME}://{API_DOMAIN}:{API_PORT}/{MEDIA_ROOT_SHORT}/{record.avatar}'

    @classmethod
    def get_token(cls, record):
        try:
            return record.auth_token.key
        except ObjectDoesNotExist:
            return None

class UserSerializerIdNameAvatarField(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "avatar_url")

    @classmethod
    def get_avatar_url(cls, record):
        if record.avatar:
            return f'{API_SCHEME}://{API_DOMAIN}:{API_PORT}/{MEDIA_ROOT_SHORT}/{record.avatar}'


class PostSerializers(serializers.ModelSerializer):
    author = UserSerializers(read_only=True)
    photo_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "description", "author", "photo_url", "created_at", "updated_at", "moderation_status")

    @classmethod
    def get_photo_url(cls, record):
        if record.photo:
            return f'{API_SCHEME}://{API_DOMAIN}:{API_PORT}/{MEDIA_ROOT_SHORT}/{record.photo}'


class CommentSerializers(serializers.ModelSerializer):
    user = UserSerializerIdNameAvatarField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "text", "created_at", "updated_at", "parent")


class TokenSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)

    class Meta:
        model = Token
        fields = ("user", "key", "created")

class LikeSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    post = PostSerializers()
    class Meta:
        model = Like
        fields = ("id", "user", "post")
