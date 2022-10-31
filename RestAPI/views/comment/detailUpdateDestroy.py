from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import CommentSerializers
from RestAPI.services.main.comment.delete import DeleteCommentService
from RestAPI.services.main.comment.update import CommentUpdateService
from main.models import Comment


class CommentDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializers

    def get(self, request, *args, **kwargs):
        return Response({"comment": CommentSerializers(Comment.objects.get(pk=kwargs['pk']), many=False).data}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        outcome = CommentUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user})
        return Response({"updated_comment": CommentSerializers(outcome, many=False).data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        message = DeleteCommentService.execute(kwargs | request.POST.dict() | {"user": request.user})
        return Response({"comment": message})

