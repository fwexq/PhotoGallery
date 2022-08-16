from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from ..models.post.models import Post


class PostInvalidView(View):
    def get(self, request, **kwargs):
        posts = get_object_or_404(Post, pk=kwargs['det'])
        print(posts)
        posts.moderation_status = 'INVALID'
        posts.save()
        return redirect('posts_list')

class PostValidView(View):
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['det'])
        print(post)
        post.moderation_status = 'VALID'
        post.publicated_at = timezone.now()
        post.save()
        return redirect('posts_list')