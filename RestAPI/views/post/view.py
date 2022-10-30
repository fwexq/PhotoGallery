from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import *


class PostsListView(generics.ListAPIView):
    serializer_class = PostSerializers

    def get(self, request, *args, **kwargs):
        return Response({"posts": PostSerializers(Post.objects.all(), many=True).data}, status=status.HTTP_200_OK)


