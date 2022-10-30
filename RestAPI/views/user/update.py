from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from RestAPI.serializers import UserSerializers
from RestAPI.services.main.accounts.profile_update import ProfileUpdateService


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        outcome = ProfileUpdateService.execute(kwargs | request.POST.dict() | {'user': request.user}, request.FILES)
        if type(outcome) == str:
            return Response({"updated_user": outcome}, status=status.HTTP_200_OK)
        else:
            return Response({"updated_user": UserSerializers(outcome).data}, status=status.HTTP_200_OK)

