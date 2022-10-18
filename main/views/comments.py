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
        parent = request.POST.get('parent', None)
        comment = post.comments.create(text=request.POST['text'], user_id=request.user.id)
        if parent:
            comment.parent = Comment.objects.get(id=int(parent))
        comment.save()
        return redirect('posts_detail', post_id=post.id)






        #
        # parent = request.POST.get('parent', None)
        # print(parent)
        # form = CommentForm(request.POST)
        # if form.is_valid():
        #     comment = form.save(commit=False)
        #     comment.post = post
        #     comment.user = request.user
        #     comment.parent = parent
        #     comment.save()
        #     return redirect('posts_detail', post_id=post.id)


 # post = Post.objects.get(pk=kwargs['post_id'])
        # post.comments.create(text=request.POST['text'], user_id=request.user.id)




# def detail(request, slug):
#   html = 'detail.html'
#   post = get_object_or_404(Post, slug=slug)
#   if request.method == "POST":
#     parent = request.POST.get('parent', None)
#     print(parent)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#       comment = form.save(commit=False)
#       comment.post = post
#       comment.user = request.user
#       comment.parent = parent
#       comment.save()
#       return redirect('detail_man_post', slug=post.slug)
#   else:
#     form = CommentForm()