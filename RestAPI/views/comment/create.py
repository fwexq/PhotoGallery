from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.comments.create import CommentsCreateService


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializers

    def post(self, request, *args, **kwargs):
        comment = CommentsCreateService.execute(request.POST.dict() | {'user': request.user} | kwargs)
        return Response({'user': CommentSerializers(comment, many=False).data}, status=status.HTTP_200_OK)