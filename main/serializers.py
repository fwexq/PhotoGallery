from rest_framework import serializers

from RestAPI.serializers import UserSerializers
from main.models import Post, Like, CustomUser, Comment


class UserSerializerIdNameAvatarField(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "avatar_url")

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializers(read_only=True)

    class Meta:
        model = Post
        fields = ("id", 'photo', "title", "description", "author", "publicated_at")


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "user", "post")


class CommentSerializers(serializers.ModelSerializer):
    user = UserSerializerIdNameAvatarField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "text", "created_at", "updated_at", "parent")