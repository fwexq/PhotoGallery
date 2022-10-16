from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView

from ..forms import *
from ..models.post.models import Post


class CommentsView(View):
    form_class = CommentForm
    model = Comment
    template_name = 'main/posts/detail.html'

    # def get(self, request, *args, **kwargs):
    #     print('1')
    #     return render(request, 'main/posts/detail.html', {'comment_form': CommentForm()})
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['post_id'])
        post.comments.create(text=request.POST['text'], user_id=request.user.id)
        return redirect('posts_detail', post_id=post.id)




