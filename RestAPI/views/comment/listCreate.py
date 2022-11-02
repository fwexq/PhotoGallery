from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.comment.create import CommentCreateService
from RestAPI.services.main.comment.list import CommentListService


class CommentListCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializers
    
    def get(self, request, *args, **kwargs):
        return Response(CommentSerializers(CommentListService.execute(kwargs).result, many=True).data,
                        status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        comment = CommentCreateService.execute(request.POST.dict() | {'user': request.user} | kwargs)
        return Response({'user': CommentSerializers(comment.result, many=False).data}, status=status.HTTP_200_OK)
