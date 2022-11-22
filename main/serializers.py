from django.forms import IntegerField
from rest_framework import serializers
from RestAPI.serializers import UserSerializers
from main.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializers(read_only=True)
    num_likes = serializers.IntegerField()
    num_comments = serializers.IntegerField()
    get_absolute_url = serializers.CharField()

    class Meta:
        model = Post
        fields = ("id", 'photo', "title", "description", "author", "publicated_at", "num_likes", "num_comments", "get_absolute_url")


# class LikeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ("id", "user", "post")
#
#
# class CommentSerializers(serializers.ModelSerializer):
#     user = UserSerializerIdNameAvatarField(read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = ("id", "user", "text", "created_at", "updated_at", "parent")