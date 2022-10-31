from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import PostSerializers
from RestAPI.services.main.posts.delete import DeletePostService
from RestAPI.services.main.posts.update import PostUpdateService
from main.models import Post


class PostDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers

    def get(self, request, *args, **kwargs): #сервис
        try:
            return Response(PostSerializers(Post.objects.get(pk=kwargs['pk'])).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        outcome = PostUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(PostSerializers(outcome.result).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        message = DeletePostService.execute(kwargs | request.POST.dict() | {"user": request.user})
        return Response({"post": message})

