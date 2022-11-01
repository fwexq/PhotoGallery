from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from RestAPI.serializers import UserSerializers
from RestAPI.services.main.user.profile_update import ProfileUpdateService


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        outcome = ProfileUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        if outcome.errors:
            return Response({key: str(error) for key, error in outcome.errors.items()}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(UserSerializers(outcome.result).data, status=status.HTTP_200_OK)

