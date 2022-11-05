from django.http import JsonResponse
from django.views import View

from main.services.main.posts.likes import LikesService


class LikesView(View):
    def post(self, request,  *args, **kwargs):
        is_likes = LikesService.execute(kwargs | {'user': request.user})
        return JsonResponse({'is_likes': is_likes})
