from rest_framework import generics, status
from rest_framework.response import Response

from RestAPI.serializers import PostSerializers
from RestAPI.services.main.posts.update import PostUpdateService


class PostDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    def patch(self, request, *args, **kwargs):
        post = PostUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        return Response({'user': PostSerializers(post, many=False).data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        post = PostUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        post = post.delete().save()
        return Response({'user': PostSerializers(post, many=False).data}, status=status.HTTP_200_OK)
