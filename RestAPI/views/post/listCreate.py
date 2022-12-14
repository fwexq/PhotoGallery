from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.post.create import CreatePostService
from RestAPI.services.main.post.list import PostListService


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializers

    def get(self, request, *args, **kwargs):
        return Response(PostSerializers(PostListService.execute(kwargs).result, many=True).data,
                        status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        outcome = CreatePostService.execute(request.data.dict() | {'user': request.user}, request.FILES)
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"post": PostSerializers(outcome.result).data}, status=status.HTTP_200_OK)
