from django.shortcuts import redirect
from django.views import View
from ..models.post.models import Post
from ..services.main.posts.likes import LikesService


class LikesView(View):
    def post(self, request,  *args, **kwargs):
        LikesService.execute(kwargs | {'user': request.user})
        return redirect('posts_detail', det=kwargs['pk'])
