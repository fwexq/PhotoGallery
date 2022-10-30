from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import *


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentSerializers

    def get(self, request, *args, **kwargs):
        return Response({"posts": CommentSerializers(Comment.objects.all(), many=True).data}, status=status.HTTP_200_OK)


