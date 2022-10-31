from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import PostSerializers
from RestAPI.services.main.post.valid_or_invalid_posts import PostInvalidService, PostValidService


class PostInvalidView(generics.ListAPIView):
    def get(self, request, **kwargs):
        outcome = PostInvalidService.execute(kwargs)
        return Response({"post": PostSerializers(outcome, many=False).data}, status=status.HTTP_200_OK)

class PostValidView(generics.ListAPIView):
    def get(self, request, **kwargs):
        outcome = PostValidService.execute(kwargs)
        return Response({"post": PostSerializers(outcome, many=False).data}, status=status.HTTP_200_OK)