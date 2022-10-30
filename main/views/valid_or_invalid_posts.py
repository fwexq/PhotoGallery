from django.shortcuts import redirect
from django.views import View
from RestAPI.services.main.posts.valid_or_invalid_posts import PostInvalidService, PostValidService


class PostInvalidView(View):
    def get(self, request, **kwargs):
        PostInvalidService.execute(kwargs)
        return redirect('posts_list')

class PostValidView(View):
    def get(self, request, **kwargs):
        PostValidService.execute(kwargs)
        return redirect('posts_list')