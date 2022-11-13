from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from main.services.main.menu.filtration import PostFiltrationService


class PostFiltrationView(View):

    def get(self, request, *args, **kwargs):
        posts = PostFiltrationService.execute(request.GET)
        return render(request, 'main/posts/list.html', {"posts": posts})

