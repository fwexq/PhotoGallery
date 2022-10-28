from django.shortcuts import redirect
from django.views import View
from RestAPI.services.main.comments.create import CommentsCreateService
from ..forms import *


class CommentsView(View):
    model = Comment

    def post(self, request, *args, **kwargs):
        CommentsCreateService.execute(request.POST.dict() | {'user': request.user} | kwargs)
        return redirect('posts_detail', post_id=kwargs['post_id'])
