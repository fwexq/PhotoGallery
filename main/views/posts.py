from django.contrib import messages
from django.db.models.fields.files import ImageFieldFile
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ..forms import *
from main.utils import DataMixin
from ..models.post.models import Post
from ..services.main.posts.create import CreatePostService
from ..services.main.posts.update import PostUpdateService


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
        comment_form = CommentForm()
        return render(request,
                      'main/posts/detail.html',
                      {'post_obj': post_obj,
                       'comments': comments,
                       'comment_form': comment_form})

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
        post_form = CreatePostForm()
        return render(request, 'main/posts/create.html', {'post_form': post_form})

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
        post = get_object_or_404(Post, pk=kwargs['post_id'])
        form = PostForm()
        # return redirect('posts_update', post_id=kwargs['post_id'])
        return render(request, 'main/posts/update.html', {'form': form, 'post': post})


class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'det'
    template_name = 'main/posts/confirm_delete.html'

    success_url = reverse_lazy('posts_list')



