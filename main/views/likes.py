from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from ..models.post.models import Post
from ..services.main.posts.likes import LikesService


class LikesView(View):
    def post(self, request,  *args, **kwargs):

        is_liked = LikesService.execute(kwargs | {'user': request.user})
        return JsonResponse({'is_liked': is_liked})
