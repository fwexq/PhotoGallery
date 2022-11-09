from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from ..services.main.posts.delete import PostDeleteService
from ..services.main.posts.update import PostUpdateService
from ..forms import *
from main.utils import DataMixin
from ..models.post.models import Post
from ..services.main.posts.create import CreatePostService


class PostListView(DataMixin, ListView):
    paginate_by = 4
    model = Post
    template_name = 'main/posts/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(moderation_status='VALID').order_by('-publicated_at')
        return posts


class DetailPostView(DataMixin, View):
    def get(self, request, *args, **kwargs):
        post_obj = Post.objects.get(pk=kwargs['post_id'])
        comments = post_obj.comments.filter(parent=None)
        return render(request,
                      'main/posts/detail.html',
                      {'post_obj': post_obj,
                       'comments': comments,
                       'comment_form': CommentForm()})

    # def comments(request):
    #     if request.method == 'POST':
    #         comment_form = CommentForm(data=request.POST)
    #         post_id = request.POST.get('post_id')
    #         post_obj = Post.objects.get(id=post_id)
    #         comments = Comment.objects.all()
    #         if comment_form.is_valid():
    #             new_comment = comment_form.save(commit=False)
    #             new_comment.post = post_obj
    #             new_comment.save()
    #     else:
    #         comment_form = CommentForm()
    #     return render(request,
    #                   'main/posts/detail.html',
    #                   {'post_obj': post_obj,
    #                    'comments': comments,
    #                    'comment_form': comment_form})


class CreatePostView(CreateView, View):
    form_class = CreatePostForm
    template_name = 'main/posts/create.html'

    def post(self, request, *args, **kwargs):
        CreatePostService.execute(request.POST.dict() | {'user': request.user}, request.FILES)
        return redirect('posts_list')

    def get(self, request, *args, **kwargs):
        return render(request, 'main/posts/create.html', {'post_form': CreatePostForm()})

class PostUpdateView(UpdateView):
    template_name = 'main/posts/update.html'
    form_class = PostForm
    context_object_name = 'post'
    # pk_url_kwarg = 'post_id'

    def post(self, request, *args, **kwargs):
        #
        PostUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)

        # form = PostForm(files=request.FILES, data=request.POST, instance=post)
        # if form.is_valid():
        #     if hasattr(form.cleaned_data['photo'], 'image'):
        #         post.previous_photo = post.photo
        #     post.moderation_status = 'NOT_MODERATED'
        #     post.publicated_at = timezone.now()
        #     post.save()

        return redirect('posts_list')

    def get(self, request, *args, **kwargs):
        # return redirect('posts_update', post_id=kwargs['post_id'])
        return render(request, 'main/posts/update.html', {'form':  PostForm(), 'post': Post.objects.get(pk=kwargs['post_id'])})


class PostDeleteView(View):
    model = Post
    def get(self, request, *args, **kwargs):
        PostDeleteService.execute(kwargs | request.POST.dict() | {'user': request.user})
        return redirect('posts_list')




# class PostDeleteView(DeleteView):
#     model = Post
#     pk_url_kwarg = 'post_id'
#     template_name = 'main/posts/confirm_delete.html'
#
#     success_url = reverse_lazy('posts_list')