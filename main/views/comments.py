from django.shortcuts import redirect
from django.views import View
from ..forms import *
from ..models.post.models import Post
from ..services.main.comments.create import CommentsCreateService


class CommentsView(View):
    model = Comment
    def post(self, request, *args, **kwargs):
        comment = CommentsCreateService.execute(request.POST.dict() | {'user': request.user} | kwargs)
        return redirect('posts_detail', post_id=kwargs['post_id'])


 # post = Post.objects.get(pk=kwargs['post_id'])
        # post.comments.create(text=request.POST['text'], user_id=request.user.i



        # post = Post.objects.get(pk=kwargs['post_id'])
        # parent = request.POST.get('parent', None)
        # comment = post.comments.create(text=request.POST['text'], user_id=request.user.id)
        # if parent:
        #     comment.parent = Comment.objects.get(id=int(parent))
        # comment.save()
        # return redirect('posts_detail', post_id=post.id)