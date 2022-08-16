from django.views.generic import ListView
from ..models.post.models import Post


class PostStatusView(ListView):
    model = Post
    template_name = 'main/posts/posts_rejected.html'
    context_object_name = 'posts'
    POST_STATUS_MAPPER = {'rejected': 'INVALID', 'published': 'VALID', 'moderated': 'NOT_MODERATED'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_type'] = self.kwargs.get('status')
        return context

    def get_queryset(self):
        moderation_status = self.POST_STATUS_MAPPER.get(self.kwargs.get('status'))
        if moderation_status:
            posts = Post.objects.filter(moderation_status=moderation_status, author=self.request.user).order_by('-created_at')
        else:
            posts = Post.objects.none()
        return posts
