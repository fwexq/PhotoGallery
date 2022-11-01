from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import PostSerializers
from RestAPI.services.main.post.delete import DeletePostService
from RestAPI.services.main.post.update import PostUpdateService
from RestAPI.services.main.post.get import PostGetService
from main.models import Post


class PostDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers

    def get(self, request, *args, **kwargs):
        outcome = PostGetService.execute(kwargs | request.POST.dict(), request.FILES)
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(PostSerializers(outcome.result).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        outcome = PostUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(PostSerializers(outcome.result).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        outcome = DeletePostService.execute(kwargs | request.POST.dict() | {'user': request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

