from rest_framework import generics, status
from rest_framework.response import Response
from RestAPI.serializers import *


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        return Response({'user': UserSerializers(self.request.user, many=False).data}, status=status.HTTP_200_OK)