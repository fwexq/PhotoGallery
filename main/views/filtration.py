from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from main.services.main.menu.filtration import PostFiltrationService


class PostFiltrationView(View):

    def post(self, request, *args, **kwargs):
        posts = PostFiltrationService.execute(request.POST)
        return render(request, 'main/posts/list.html', {"posts": posts})

