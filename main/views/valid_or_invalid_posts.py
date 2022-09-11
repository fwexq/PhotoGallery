from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from ..models.post.models import Post
from ..services.main.posts.valid_or_invalid_posts import PostInvalidService, PostValidService


class PostInvalidView(View):
    def get(self, request, **kwargs):
        PostInvalidService.execute(kwargs)
        # posts = get_object_or_404(Post, pk=kwargs['det'])
        # posts.moderation_status = 'INVALID'
        # posts.save()
        return redirect('posts_list')

class PostValidView(View):
    def get(self, request, **kwargs):
        PostValidService.execute(kwargs)
        # post = get_object_or_404(Post, pk=kwargs['det'])
        # post.moderation_status = 'VALID'
        # post.publicated_at = timezone.now()
        # post.save()
        return redirect('posts_list')