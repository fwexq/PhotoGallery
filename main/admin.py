from django.contrib import admin
from django.utils.safestring import mark_safe

from main.models.like.models import Like
from main.models.post.models import Post
from main.models.user.models import CustomUser
from main.models.comment.models import Comment

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'last_name', 'password', 'avatar', 'created_at', 'updated_at')
admin.site.register(CustomUser, CustomUserAdmin)


class PostAdmin(admin.ModelAdmin):
    # fields = ['liked']
    # list_display = ('title', 'description', 'created_at', 'updated_at', 'publicated_at', 'moderation_status', 'publish', 'photo', 'photo_now', 'previous_photo')
    fields = ['title', 'description', 'publicated_at', 'moderation_status', 'publish', 'photo', 'photo_now', 'previous_photo', 'old_photo']
    readonly_fields = ["photo_now", "old_photo"]

    def photo_now(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}">')

    def old_photo(self, obj):
        return mark_safe(f'<img src="{obj.previous_photo.url}">')

    # def has_add_permission(self, request):
    #     return False
admin.site.register(Post, PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    def has_add_permission(self, request):
        return False
admin.site.register(Like, LikeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user', 'text')
admin.site.register(Comment, CommentAdmin)