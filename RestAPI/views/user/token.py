from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from RestAPI.serializers import TokenSerializers
from RestAPI.services.main.accounts.token import TokenService


class UserCreateTokenView(generics.CreateAPIView):

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        outcome = TokenService.execute(kwargs | {'user': request.user})
        if type(outcome) == str:
            return Response({"token": outcome}, status=status.HTTP_200_OK)
        else:
            return Response({"token": TokenSerializers(outcome, many=False).data}, status=status.HTTP_200_OK)