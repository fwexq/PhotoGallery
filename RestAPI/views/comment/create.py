from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.comment.create import CommentsCreateService
from RestAPI.services.main.comment.get import CommentListService


class CommentAddListView(generics.CreateAPIView):
    serializer_class = CommentSerializers
    
    def get(self, request, *args, **kwargs):
        outcome = CommentListService.execute(kwargs)
        try:
            return Response(CommentSerializers(outcome.result).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        comment = CommentsCreateService.execute(request.POST.dict() | {'user': request.user} | kwargs)
        return Response({'user': CommentSerializers(comment, many=False).data}, status=status.HTTP_200_OK)
