from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import PostSerializers
from RestAPI.services.main.posts.delete import DeletePostService
from RestAPI.services.main.posts.update import PostUpdateService
from main.models import Post


class PostDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers

    def get(self, request, *args, **kwargs):
        return Response({"post": PostSerializers(Post.objects.get(pk=kwargs['pk']), many=False).data}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        outcome = PostUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        return Response({"updated_post": PostSerializers(outcome, many=False).data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        message = DeletePostService.execute(kwargs | request.POST.dict() | {"user": request.user})
        return Response({"post": message})

