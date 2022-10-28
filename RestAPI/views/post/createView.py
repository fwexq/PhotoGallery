from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.posts.create import CreatePostService


class PostAddListView(generics.ListCreateAPIView):
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return Response({"posts": PostSerializers(posts, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        outcome = CreatePostService.execute(request.data.dict() | {'user': request.user}, request.FILES)
        return Response({"post": PostSerializers(outcome).data}, status=status.HTTP_200_OK)

