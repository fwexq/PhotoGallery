from django.shortcuts import redirect
from django.views.generic import ListView
from ..forms import *
from ..models.post.models import Post


class PostModerationListView(ListView):
    model = Post
    template_name = 'main/posts/list_for_moderators.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Объявления без модерации'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('posts_list')

    def get_queryset(self):
        posts = Post.objects.filter(moderation_status='NOT_MODERATED').order_by('-created_at')
        return posts
