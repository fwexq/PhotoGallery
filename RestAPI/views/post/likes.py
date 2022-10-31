# from rest_framework import generics, status
# from rest_framework.response import Response
#
# from RestAPI.serializers import LikeSerializers
# from RestAPI.services.main.posts.likes import LikesService
#
#
# class PostAddLikeView(generics.CreateAPIView):
#     serializer_class = LikeSerializers
#     def post(self, request, *args, **kwargs):
#         is_liked = LikesService.execute(kwargs | {'user': request.user})
#         return Response({"post": LikeSerializers(is_liked, many=False).data}, status=status.HTTP_200_OK)