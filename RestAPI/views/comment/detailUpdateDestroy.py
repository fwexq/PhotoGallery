from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import CommentSerializers
from RestAPI.services.main.comment.delete import DeleteCommentService
from RestAPI.services.main.comment.get import CommentDetailService
from RestAPI.services.main.comment.update import CommentUpdateService


class CommentDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializers

    def get(self, request, *args, **kwargs):
        outcome = CommentDetailService.execute(kwargs)
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(CommentSerializers(outcome.result).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        outcome = CommentUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(CommentSerializers(outcome.result).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        outcome = DeleteCommentService.execute(kwargs | request.POST.dict() | {"user": request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

