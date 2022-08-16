from django.shortcuts import redirect
from django.views import View
from ..forms import *
from ..models.post.models import Post


class CommentsView(View):
    form_class = CommentForm
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['det'])
        post.comments.create(text=request.POST['text'], user_id=request.user.id)
        return redirect('posts_detail', det=post.id)
