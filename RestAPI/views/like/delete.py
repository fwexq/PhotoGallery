from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import LikeSerializers
from RestAPI.services.like.delete import DeleteLikeService


class PostDeleteLikeView(generics.DestroyAPIView):
    serializer_class = LikeSerializers

    def delete(self, request, *args, **kwargs):
        outcome = DeleteLikeService.execute(kwargs | {'user': request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
