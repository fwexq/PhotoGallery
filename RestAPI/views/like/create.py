from rest_framework import generics, status
from rest_framework.response import Response

from RestAPI.serializers import LikeSerializers
from RestAPI.services.like.create import LikeService


class PostAddLikeView(generics.CreateAPIView):
    serializer_class = LikeSerializers
    def post(self, request, *args, **kwargs):
        outcome = LikeService.execute(kwargs | {'user': request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(LikeSerializers(outcome.result).data, status=status.HTTP_200_OK)

