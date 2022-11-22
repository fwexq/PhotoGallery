from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response

from main.serializers import PostSerializer
from main.services.main.menu.filtration import PostFiltrationService


class PostFiltration(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        outcome = PostFiltrationService.execute(self.request.query_params.dict())
        return Response({'posts': PostSerializer(outcome, many=True).data})
        # posts = self.request.GET('sort', "")
        # posts = PostFiltrationService.execute(request.GET)
        # return render(request, 'main/posts/list.html', {"posts": posts})





# class PostFiltrationView(View):
#
#     def get(self, request, *args, **kwargs):
#         posts = PostFiltrationService.execute(request.GET)
#         return render(request, 'main/posts/list.html', {"posts": posts})
