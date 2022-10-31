from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestAPI.serializers import *
from RestAPI.services.main.user.get import UserGetService
from RestAPI.services.main.user.token import TokenService


class UserDetailView(generics.ListCreateAPIView):
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        outcome = UserGetService.execute({"user": request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(UserSerializers(outcome.result).data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        outcome = TokenService.execute(kwargs | {'user': request.user})
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(UserSerializers(outcome.result).data, status=status.HTTP_200_OK)
