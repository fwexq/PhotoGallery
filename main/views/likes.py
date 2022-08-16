from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from ..models.post.models import Post

class LikesView(View):
    def post(self, request,  *args, **kwargs):
        user = request.user
        post_obj = Post.objects.get(pk=kwargs['pk'])
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
            is_liked = False
        else:
            post_obj.liked.add(user)
            is_liked = True
        post_obj.save()
        return JsonResponse({'is_liked': is_liked})
