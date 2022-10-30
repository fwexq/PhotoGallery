from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.posts.create import CreatePostService


class PostAddView(generics.ListCreateAPIView):
    serializer_class = PostSerializers

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        outcome = CreatePostService.execute(request.data.dict() | {'user': request.user}, request.FILES)
        if type(outcome) == str:
            return Response({"post": outcome}, status=status.HTTP_200_OK)
        else:
            return Response({"post": PostSerializers(outcome).data}, status=status.HTTP_200_OK)

